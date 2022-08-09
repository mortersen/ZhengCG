from PyQt5.QtWidgets import QWidget,QListWidget,QListWidgetItem,QVBoxLayout
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import QSize

from UI.UI_CustomItem import Ui_CustomItem
from UI.UI_HMCSearchWidget import Ui_HMCSearch

class HMCSearchWidget(QWidget):
    from ZhengCGMain import MainWindow
    def __init__(self,mainWindow=MainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        self.md5List = []
        self.query = QSqlQuery(self.mainWindow.DB)
        self.ui = Ui_HMCSearch()
        self.ui.setupUi(self)

        self.vboxLayout = QVBoxLayout(self)
        self.ui.listWidget.setLayout(self.vboxLayout)

        #信号绑定
        self.ui.pushButton_Search.clicked.connect(self.on_search)

    #槽，响应搜素
    def on_search(self):
        keyWords = self.ui.lineEdit_Context.text().strip()
        if keyWords == '':
            return
        context =  "SELECT * FROM HMCINFO WHERE MAINTEXT LIKE \'%%%s%%\'" % keyWords
        self.query.exec(context)
        self.query.last()
        count = self.query.at() + 1
        self.ui.label_Status.setText("检索“" + keyWords + "”" + "共获记录" + str(count) + "条。")
        if count <= 0 :
            return
        self.md5List=[]
        self.ui.listWidget.clear()
        heigth = self.ui.listWidget.height()//2
        width = self.ui.listWidget.width() - 30
        print(heigth)
        print(width)
        for i in range(count):
            self.query.seek(i)
            self.md5List.append(self.query.value("MD5"))
            widget = CustomItem()
            widget.AssignItem(self.query.value("TITLENAME"),self.query.value("MAINTEXT"),self.query.value("BOOKNAME"),self.query.value("VOLUME"),self.query.value("FILELABEL"),self.query.value("PAGES"),str(i+1))
            item = QListWidgetItem()
            item.setSizeHint(QSize(width,heigth))
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item,widget)

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
        self.ui.label_MainText.setText(mainText)
        self.ui.label_MainText.adjustSize()
        self.ui.label_BookName.setText('《' + book + '》')
        self.ui.label_FileLabel.setText(file)
        self.ui.label_Volume.setText(volume + "册")
        self.ui.label_Pages.setText('页码：' + pages)



