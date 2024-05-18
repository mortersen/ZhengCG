import os
from threading import Thread
from PyQt5.QtWidgets import QWidget,QAbstractItemView,QMessageBox,QDataWidgetMapper,QFileDialog
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

from ZhengCGMain import MainWindow
from PDFWidget import WidgetPDFStream

from UI.UI_HMCListWidget import Ui_HMCListWidget


class HMCListWidget(QWidget):

    signal_SaveOver = pyqtSignal(str)

    def __init__(self,mainWin=MainWindow,DB=QSqlDatabase):
        super().__init__()
        self.ui = Ui_HMCListWidget()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        # 设置地区结构树展开
        self.ui.treeWidgetClass.expandAll()
        # 隐藏第一列
        self.ui.treeWidgetClass.hideColumn(1)

        #初始化数据库对应表显示

        #用于查询
        self.DB = DB
        self.DB.open()
        self.sqlQuery = QSqlQuery(self.DB)

        #用于同步表格,及控件
        self.qryModel = QSqlQueryModel(self)
        self.ui.tableView.setModel(self.qryModel)
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.qryModel)

        self.currentPage = 0
        self.eachRecordPerPage = 10
        self.totalRecord = self.countRecord('')
        self.ui.labelTotalRecord.setText("总"+str(self.totalRecord)+"条记录")
        self.pages = self.countPages()
        self.ui.labelPages.setText(str(self.pages))

        self.updateLabel()
        self.query = "SELECT FILELABEL,BOOKNAME,TITLENAME,MAINTEXT,QUOTE,VOLUME,PAGES,FL1ST,FL2ND,MD5 FROM HMCINFO"
        self.condition = ""
        self.executeQurey(self.currentPage*self.eachRecordPerPage)
        self.initTable()

        #设置信号
        #目录树选择切换
        self.ui.treeWidgetClass.clicked.connect(self.switchClass_callback)
        #前一页
        self.ui.pbnUppage.clicked.connect(self.UpPage_Callback)
        #h后一页
        self.ui.pbnDownpage.clicked.connect(self.DoPage_Callback)

        #跳转页面
        self.ui.pbnGotoPage.clicked.connect(self.GotoPage_Callback)
        self.ui.lineEditGotoPage.returnPressed.connect(self.GotoPage_Callback)

        #槽，响应改变表格选择行事件
        self.selectionModel = self.ui.tableView.selectionModel()
        self.selectionModel.currentRowChanged.connect(self.do_currentRowChanged)

        #双击表格阅读歌册文档PDF
        self.ui.tableView.doubleClicked.connect(self.do_readSongZaiPDF)

        #单击阅读按钮阅读歌册文档PDF
        self.ui.ptnRead.clicked.connect(self.do_read)

        #单击下载按钮下载歌册PDF
        self.ui.pbnDownload.clicked.connect(self.do_download)

        #槽，按关键字搜索
        self.ui.pbnSearch.clicked.connect(self.do_searchKeyworld)
        self.ui.lineEditKeyWorld.returnPressed.connect(self.do_searchKeyworld)


        #信号,重新载入数据库
        self.ui.pbnReload.clicked.connect(self.do_reloadDB)

        # 槽，信号绑定下载完成提示函数
        self.signal_SaveOver.connect(self.onSignalSaveOver)


    # 初始化表格
    def initTable(self):
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        # 设置默认行高
        self.ui.tableView.verticalHeader().setDefaultSectionSize(120)
        #设置默认宽度
        self.ui.tableView.setColumnWidth(0, 150)
        self.ui.tableView.setColumnWidth(1, 120)
        self.ui.tableView.setColumnWidth(3, 400)
        self.ui.tableView.setColumnWidth(4, 100)
        self.ui.tableView.setColumnWidth(5, 80)
        self.ui.tableView.setColumnWidth(6, 80)
        self.ui.tableView.setColumnWidth(7, 100)
        self.ui.tableView.setColumnWidth(8, 100)
        #设置隐藏列
        self.ui.tableView.setColumnHidden(9, True)


        self.qryModel.setHeaderData(0, Qt.Horizontal, "卷名")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "书名")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "题名")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "正文")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "摘录")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "卷")
        self.qryModel.setHeaderData(6, Qt.Horizontal, "页码")
        self.qryModel.setHeaderData(7, Qt.Horizontal, "一级分类")
        self.qryModel.setHeaderData(8, Qt.Horizontal, "二级分类")

        self.mapper.addMapping(self.ui.lineEditClass1,7)
        self.mapper.addMapping(self.ui.lineEditClass2,8)
        self.mapper.addMapping(self.ui.lineEditQuote,4)
        self.mapper.addMapping(self.ui.lineEditPages,6)
        self.mapper.addMapping(self.ui.lineEditVolume,5)
        self.mapper.addMapping(self.ui.textEditMainText, 3)
        self.mapper.addMapping(self.ui.lineEditTitleName, 2)
        self.mapper.addMapping(self.ui.lineEditBookName, 1)
        self.mapper.addMapping(self.ui.lineEditFileLabel, 0)


        self.mapper.toFirst()


    #计算总记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from HMCINFO" + condition
        #print(SqlTotoalQuery)
        try:
            self.sqlQuery.exec(SqlTotoalQuery)
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception.__str__())

    #计算总页数
    def countPages(self):
        if self.totalRecord > 0:
            if self.totalRecord > self.eachRecordPerPage:
                countPages = self.totalRecord//self.eachRecordPerPage
                if  self.totalRecord % self.eachRecordPerPage !=0:
                    return countPages + 1
                else:
                    return countPages
            else:
                return  1
        else:
            return 1


    #刷新标签
    def updateLabel(self):
        self.ui.labelCurrentPage.setText(str(self.currentPage+1))
        self.ui.labelPages.setText(str(self.pages))
        self.ui.labelTotalRecord.setText("总{0}条记录".format(str(self.totalRecord)))

    #执行查询page
    def executeQurey(self, index):
        limit = " limit %d,%d" % (index, self.eachRecordPerPage)
        query = self.query + self.condition + limit
        self.qryModel.setQuery(query)

    #槽，目录树切换分类
    def switchClass_callback(self):
        item = self.ui.treeWidgetClass.currentItem().text(0)
        if item == '文献史料汇编库':
            self.condition = ""
        else:
            if item  ==  "石刻、碑刻文献" or item  ==  "族谱" or item  ==  "东亚地区文献" or item  ==  "欧美文献" :
                self.condition = " WHERE FL2ND LIKE \'%%%s%%\' " % (item)
            else:
                self.condition = " WHERE FL1ST LIKE \'%%%s%%\' " % (item)

        self.totalRecord = self.countRecord(self.condition)
        self.pages = self.countPages()
        self.currentPage = 0
        self.executeQurey(0)
        self.updateLabel()

    #槽，上一页
    def UpPage_Callback(self):
        if self.currentPage == 0:
            return
        self.currentPage = self.currentPage - 1
        self.executeQurey(self.currentPage * self.eachRecordPerPage)
        self.updateLabel()

    #槽，下一页
    def DoPage_Callback(self):
        if self.currentPage + 1== self.pages:
            return
        self.currentPage = self.currentPage + 1
        self.executeQurey(self.currentPage * self.eachRecordPerPage)
        self.updateLabel()

    #槽，跳转页面
    def GotoPage_Callback(self):
        target = self.ui.lineEditGotoPage.text().strip()
        if target.isnumeric() is False:
            QMessageBox.warning(self, "警告", "请输入正确的页码数字!", QMessageBox.Yes)
            self.ui.lineEditGotoPage.setText("")
            return
        targetPage = int(target)
        if targetPage < 1 or targetPage > self.pages:
            QMessageBox.warning(self, "警告", "请输入正确的页码数字!", QMessageBox.Yes)
            self.ui.lineEditGotoPage.setText("")
        else:
            self.currentPage = targetPage - 1
            self.executeQurey(self.currentPage * self.eachRecordPerPage)
            self.updateLabel()

    #槽，响应表格行选择改变
    def do_currentRowChanged(self,current,previous):
        self.mapper.setCurrentIndex(current.row())

    #槽，响应双击阅读歌册
    def do_readSongZaiPDF(self,index):
        curRec = self.qryModel.record(index.row())
        Title = curRec.value("BOOKNAME")
        MD5 = curRec.value("MD5")
        if MD5 is None:
            QMessageBox.information(self, "提示", "未收录该文档资料!")
        else:
            bin = self.getPDFStream(MD5)
            tab = WidgetPDFStream(bin,Title)
            self.mainWin.cenTab.addTab(tab, QIcon(":/PIC/阅读.png"), Title[0:12])
            self.mainWin.cenTab.setCurrentWidget(tab)

    #槽，按阅读按钮阅读
    def do_read(self):
        if (self.ui.tableView.currentIndex().row()) < 0:
            return
        self.do_readSongZaiPDF(self.ui.tableView.currentIndex())


    #槽，响应关键字搜索
    def do_searchKeyworld(self):
        keyworld = self.ui.lineEditKeyWorld.text().strip()

        if len(keyworld) == 0:
            QMessageBox.information(self, "提示", "请输入搜索关键字!", QMessageBox.Yes)
            return
        else:
            condition = " WHERE QUOTE LIKE \'%%%s%%\' or FILELABEL LIKE \'%%%s%%\' or BOOKNAME LIKE \'%%%s%%\' or TITLENAME LIKE \'%%%s%%\' or MAINTEXT LIKE \'%%%s%%\'" % (keyworld,keyworld,keyworld,keyworld,keyworld)
            #print(condition)
            sen = self.query + condition
            try:
                self.sqlQuery.exec(sen)
                self.sqlQuery.last()
                count = self.sqlQuery.at() + 1
                # print(count)
            except Exception:
                print(Exception.__str__())
            #print(sen)
            if count == -1 :
                QMessageBox.information(self, "提示", "关键字：\"" + keyworld + "\"查无记录", QMessageBox.Yes)
                return
            else:
                self.totalRecord = count
                self.pages = self.countPages()
                self.currentPage = 0
                self.condition = condition
                self.executeQurey(self.currentPage)
                self.updateLabel()
                QMessageBox.information(self, "提示", "查询符合关键字：\"" + keyworld + "\"\n共"+str(count)+"条！", QMessageBox.Yes)


            return


    #槽，响应重新载入数据库操作
    def do_reloadDB(self):
        self.condition = ''
        self.condition = ''
        self.totalRecord = self.countRecord('')
        self.pages = self.countPages()
        self.currentPage = 0
        self.updateLabel()
        self.ui.lineEditKeyWorld.setText('')
        self.ui.lineEditGotoPage.setText('')
        self.executeQurey(self.currentPage)


    # 阅读辅助函数，负责查询，辅助返回PDF流，提供阅读或下载PDF函数使用
    def getPDFStream(self, md5):
        Query = "select FILEBINARY from HMCFILE where MD5=?"
        self.sqlQuery.prepare(Query)
        self.sqlQuery.bindValue(0, md5)
        self.sqlQuery.exec()
        self.sqlQuery.last()
        return self.sqlQuery.value("FILEBINARY")


    # 下载PDF
    def do_download(self):
        if (self.ui.tableView.currentIndex().row()) < 0:
            return
        curRec = self.qryModel.record(self.ui.tableView.currentIndex().row())
        Title = curRec.value("BOOKNAME")
        MD5 = curRec.value("MD5")
        filePath, fname = os.path.split(os.path.abspath("./" + Title + ".pdf"))
        newfileName, ok = QFileDialog.getSaveFileName(self, "文件下载到", fname, "*.pdf")
        # print(newfileName)
        if ok:
            def func():
                with open(newfileName, 'wb') as wbf:
                    fileBinary = self.getPDFStream(MD5)
                    wbf.write(fileBinary)
                self.signal_SaveOver.emit(fname)

            saveThread = Thread(target=func)
            saveThread.start()
        else:
            return

    #槽，响应下载完成
    def onSignalSaveOver(self, title):
        QMessageBox.information(self, "提示", title + "文件下载成功！")