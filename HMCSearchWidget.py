from PyQt5.QtWidgets import QWidget,QListWidgetItem,QVBoxLayout,QMessageBox
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import QSize,pyqtSignal

from threading import Thread
from queue import Queue

from UI.UI_CustomItem import Ui_CustomItem
from UI.UI_HMCSearchWidget import Ui_HMCSearch

from PDFWidget import WidgetPDFStream

records = 10

class HMCSearchWidget(QWidget):
    #自定义信号，获得从数据库读取了数据
    signal_HaveDBData = pyqtSignal()

    from ZhengCGMain import MainWindow
    def __init__(self,mainWindow=MainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        #设置辅助常量
        self.md5List = []
        self.imageQueue = Queue()
        self.currentPage = 0
        self.pages = 1
        self.keyWords = ''
        self.query = QSqlQuery(self.mainWindow.DB)

        self.ui = Ui_HMCSearch()
        self.ui.setupUi(self)

        self.vboxLayout = QVBoxLayout(self)
        self.ui.listWidget.setLayout(self.vboxLayout)

        self.setPageBtnsEnabled(False)
        #信号绑定
        self.ui.pushButton_Search.clicked.connect(self.on_search)
        self.ui.pbtHeaderPage.clicked.connect(self.on_toHeaderPage)
        self.ui.pbtDownPage.clicked.connect(self.on_toNextPage)
        self.ui.pbtUpPage.clicked.connect(self.on_toPrePage)
        self.ui.pbtBottomPage.clicked.connect(self.on_toLastPage)
        self.ui.listWidget.doubleClicked.connect(self.on_openPdftoRead)
        self.ui.lineEdit_Context.returnPressed.connect(self.on_search)

        self.signal_HaveDBData.connect(self.onSignalHaveDBDataDisplayList)

    #槽，响应搜素
    def on_search(self):
        keyWords = self.ui.lineEdit_Context.text().strip()
        #没有输入搜索字词退出
        if keyWords == '':
            QMessageBox.warning(self,"提示！","请输入检索的关键字词！",QMessageBox.Yes)
            return

        #计算检索出的记录数
        context =  "SELECT 1 FROM HMCINFO WHERE MAINTEXT LIKE \'%%%s%%\'" % keyWords
        self.query.exec(context)
        self.query.last()
        count = self.query.at() + 1

        #查不到结果
        if count <= 0 :
            self.ui.label_Status.setText("检索“" + keyWords + "”" + "无相关记录。")
            self.keyWords = ''
            self.ui.listWidget.clear()
            self.setPageBtnsEnabled(False)
            self.pages = 1
            self.currentPage = 0
            self.setPageLabel()
            return
        self.ui.label_Status.setText("检索“" + keyWords + "”" + "共获记录" + str(count) + "条。")
        self.keyWords = keyWords
        self.pages = self.caculatePages(count)
        self.currentPage = 0
        self.setPageLabel()
        self.setPageBtnsEnabled(True)

        #多线程方式加载第一页
        GetDBDataThread = Thread(target=self.getDataFromDB,args=(keyWords,self.currentPage))
        GetDBDataThread.start()


    #从数据库获取记录到内存
    def getDataFromDB(self,keyWords=str, page=int):
        context = self.queryPerPage(keyWords,page)
        self.query.exec(context)
        self.query.last()
        for i in range(self.query.at() + 1):
            self.query.seek(i)
            tempDict = {'index':str(page*records + i + 1),'title':self.query.value("TITLENAME"), 'maintext':self.query.value("MAINTEXT"),'book': self.query.value("BOOKNAME"),'volume': self.query.value(
            "VOLUME"),'filefabel': self.query.value("FILELABEL"),'pages': self.query.value("PAGES"),'md5':self.query.value('MD5'),}
            self.imageQueue.put(tempDict)
        self.signal_HaveDBData.emit()

    #将内存中数据更新UI
    def onSignalHaveDBDataDisplayList(self):
        self.md5List = []
        self.ui.listWidget.clear()
        heigth = self.ui.listWidget.height() // 2
        width = self.ui.listWidget.width() - 30
        while self.imageQueue.qsize() != 0:
            tempDict = self.imageQueue.get()
            self.md5List.append(tempDict['md5'])
            widget = CustomItem()
            widget.AssignItem(tempDict['title'],tempDict['maintext'],tempDict['book'],tempDict['volume'],tempDict['filefabel'],tempDict['pages'],tempDict['index'])
            item = QListWidgetItem()
            item.setSizeHint(QSize(width, heigth))
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)



    #生成按页码的查询语句
    def queryPerPage(self,keyWords,page):
        return "SELECT * FROM HMCINFO WHERE MAINTEXT LIKE \'%%%s%%\' LIMIT %d , %d" % (keyWords,page*records,records)

    #设置按钮可操作性
    def setPageBtnsEnabled(self,b=bool):
        self.ui.pbtHeaderPage.setEnabled(b)
        self.ui.pbtUpPage.setEnabled(b)
        self.ui.pbtDownPage.setEnabled(b)
        self.ui.pbtBottomPage.setEnabled(b)

    #多线程方式至首页
    def on_toHeaderPage(self):
        self.currentPage = 0
        self.setPageLabel()
        ToHeaderPageThread = Thread(target=self.getDataFromDB, args=(self.keyWords, self.currentPage))
        ToHeaderPageThread.start()

    #多线程方式至最末页
    def on_toLastPage(self):
        self.currentPage = self.pages - 1
        self.setPageLabel()
        ToLastPageThread = Thread(target=self.getDataFromDB, args=(self.keyWords, self.currentPage))
        ToLastPageThread.start()

    #多线程方式至下一页
    def on_toNextPage(self):
        if self.currentPage + 1 > self.pages - 1:
            return
        self.currentPage += 1
        self.setPageLabel()
        ToNextPageThread = Thread(target=self.getDataFromDB, args=(self.keyWords, self.currentPage))
        ToNextPageThread.start()

    #多线程方式至上一页
    def on_toPrePage(self):
        if self.currentPage == 0:
            return
        self.currentPage -= 1
        self.setPageLabel()
        ToPrePageThread = Thread(target=self.getDataFromDB, args=(self.keyWords, self.currentPage))
        ToPrePageThread.start()

    #计算页码数
    def caculatePages(self,count):
        base = count//records
        if count%records != 0:
            return base + 1
        return base

    #显示页码信息
    def setPageLabel(self):
        self.ui.labelPageStatus.setText(str(self.currentPage + 1) + '/' + str(self.pages))

    #槽，响应双击打开文档阅读
    def on_openPdftoRead(self):
        md5 = self.md5List[self.ui.listWidget.currentRow()]
        bin = self.getPDFStream(md5)
        book ,title = self.getPDFTitle(md5)
        if bin != None:
            tab = WidgetPDFStream(bin,book + '('+title+')')
            self.mainWindow.cenTab.addTab(tab,"【阅】"+title[0:12])
            self.mainWindow.cenTab.setCurrentWidget(tab)
        else:
            QMessageBox.information(self,"提示","找不到文档文件。")

    # 查询，辅组返回PDF流，提供阅读PDF函数使用
    def getPDFStream(self, md5):
        sqQuery = "SELECT FILEBINARY FROM HMCFILE WHERE MD5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, md5)
        self.query.exec()
        self.query.last()
        return self.query.value("FILEBINARY")

    #查询，返回书名和标题组，提供阅读PDF使用
    def getPDFTitle(self,md5):
        sqQuery = "SELECT BOOKNAME, TITLENAME FROM HMCINFO WHERE MD5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, md5)
        self.query.exec()
        self.query.last()
        return "《" + self.query.value("BOOKNAME") + '》', self.query.value("TITLENAME")

#自定义列表项类
class CustomItem(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomItem()
        self.ui.setupUi(self)

    #赋值构造Item
    def AssignItem(self,title=str, mainText=str, book=str, volume=str, file=str, pages=str, num=int):
        self.ui.label_TitleName.setText(">>>" + title.strip() + '<<<')
        self.ui.label_Num.setText(str(num))
        self.ui.label_MainText.adjustSize()
        self.ui.label_MainText.setText(mainText)

        self.ui.label_BookName.setText('《' + book.strip() + '》')
        self.ui.label_FileLabel.setText(file)
        self.ui.label_Volume.setText(volume + "册")
        self.ui.label_Pages.setText('页码：' + pages)



