import sys,hashlib
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QTabWidget,QMessageBox,QDialog

from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

from UI.UI_MainWindow import Ui_mainWindow
from UI.UI_IndexWidget import Ui_IndexWidget
from UI.UI_DetailWidget import Ui_DetailWidget
from UI.UI_TableViewWidget import Ui_ViewDBWidget
from UI.UI_AboutDialog import Ui_AboutDialog
from UI.UI_LoadSys import Ui_LoadingDialog
from UI.UI_Catalog import Ui_Catalog

from RecordDetailView import RecordDetailView
from SearchView import SearchWidget
from DBTreeView import YWDBTreeWidget,DADBTreeWidget,GDDBTreeWidget,XDDBTreeWidget
from PDFWidget import WidgetPDFStream
from ManageData import ManageWidget



def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    #print(m.hexdigest())
    return m.hexdigest()

class CatalogWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Catalog()
        self.ui.setupUi(self)


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.ui.btn_OK.released.connect(self.close)

class LoadSys(QDialog):
    Signal_CreateSetupWidget = pyqtSignal()
    def __init__(self,query=QSqlQuery):
        super().__init__()
        self.query = query
        self.ui = Ui_LoadingDialog()
        self.ui.setupUi(self)
        self.ui.btn_cancel.released.connect(self.close)

        self.ui.lineEdit_pwd.returnPressed.connect(self.on_sumbit)
        self.ui.btn_submit.released.connect(self.on_sumbit)

    def on_sumbit(self):
        try:
            pwd = self.ui.lineEdit_pwd.text()
            if pwd == "":
                QMessageBox.information(self,"提示","密码不能为空！",QMessageBox.Ok)
                return None
            else:
                pwdMD5 = md5(pwd)
                self.query.prepare("SELECT 1 FROM PWD WHERE MD5=:md5Code")
                self.query.bindValue(":md5Code",pwdMD5)
                self.query.exec()
                self.query.last()
                size = self.query.at() + 1
                if size>0:
                    self.Signal_CreateSetupWidget.emit()
                    self.close()
                else:
                    QMessageBox.critical(self, "提示", "密码错误！", QMessageBox.Ok)
                    return None
        except Exception:
            print(Exception.__str__())

#详细资料类
class DetailWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DetailWidget()
        self.ui.setupUi(self)


#数据表格显示类
class TableViewWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ViewDBWidget()
        self.ui.setupUi(self)



class IndexWidget(QWidget):

    Signal_OpebDB = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_IndexWidget()
        self.ui.setupUi(self)

        self.ui.btn_YuwaiDB.released.connect(self.on_sendSignalOpenYW)
        self.ui.btn_DanganDB.released.connect(self.on_sendSignalOpenDA)
        self.ui.btn_GudaiDB.released.connect(self.on_sendSignalOpenGD)
        self.ui.btn_XiandaiDB.released.connect(self.on_sendSignalOpenXD)
        self.ui.btn_HCMDB.released.connect(self.on_sendSignalOpenHCMDB)

    def on_sendSignalOpenYW(self):
        self.Signal_OpebDB.emit(1)

    def on_sendSignalOpenDA(self):
        self.Signal_OpebDB.emit(2)

    def on_sendSignalOpenGD(self):
        self.Signal_OpebDB.emit(3)

    def on_sendSignalOpenXD(self):
        self.Signal_OpebDB.emit(4)

    def on_sendSignalOpenHCMDB(self):
        self.Signal_OpebDB.emit(5)

#主体窗口类
class MainWindow(QMainWindow):
    #初始化
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        #初始化数据库，并链接
        self.DB = None
        self.createDB()
        self.query = QSqlQuery(self.DB)

        #设置标签主显示页
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        #初始化主页面
        self.indexTab = IndexWidget()
        self.indexTab.Signal_OpebDB.connect(self.on_openDBView)
        #初始化检索页面
        self.searchTab = SearchWidget(self.DB)
        self.searchTab.SignalViewDetailRecord.connect(self.on_OpenDetailView)

        #初始化汇编文件检索页面
        from HMCSearchWidget import HMCSearchWidget
        self.HMCTab = HMCSearchWidget(self)

        #初始话汇编文档目录页面
        from HMCListWidget import HMCListWidget
        self.CatalogTab = HMCListWidget(self,self.DB)

        #初始化四个子库
        self.yuwaiTab = YWDBTreeWidget(self.DB)
        self.yuwaiTab.Signal_ViewDetailRecord.connect(self.on_OpenDetailView)
        self.gudaiTab = GDDBTreeWidget(self.DB)
        self.gudaiTab.Signal_ViewDetailRecord.connect(self.on_OpenDetailView)
        self.xiandaiTab = XDDBTreeWidget(self.DB)
        self.xiandaiTab.Signal_ViewDetailRecord.connect(self.on_OpenDetailView)
        self.danganTab = DADBTreeWidget(self.DB)
        self.danganTab.Signal_ViewDetailRecord.connect(self.on_OpenDetailView)
        self.setupTab = None


        #工具栏，按钮动作
        self.ui.action_Search.triggered.connect(self.setSearchWidgetOpen)
        self.ui.action_Index.triggered.connect(self.setIndexWidget)
        self.ui.action_YuWai.triggered.connect(lambda :self.on_openDBView(1))
        self.ui.action_DanAnWenWu.triggered.connect(lambda :self.on_openDBView(2))
        self.ui.action_GuDaiShi.triggered.connect(lambda: self.on_openDBView(3))
        self.ui.action_XianDai.triggered.connect(lambda :self.on_openDBView(4))
        self.ui.action_Close.triggered.connect(self.on_closeAllTabs)
        self.ui.action_Setup.triggered.connect(self.on_setupTabs)
        self.ui.action_about.triggered.connect(self.on_About)
        self.ui.action_HMCSearch.triggered.connect(self.on_HMCSearch)
        self.ui.action_Catalog.triggered.connect(self.on_Catalog)

        #启动程序后，通过信号机制先载入起始页
        self.ui.action_Index.triggered.emit()

    # 启动辅助，链接数据库
    def createDB(self):
        if self.DB:
            return
        try:
            self.DB = QSqlDatabase.addDatabase("QSQLITE")
            self.DB.setDatabaseName("DB/ZhengCG.db")
           #print("Open DB success!")
        except Exception as e:
            QMessageBox.critical(self, "错误", "数据库驱动错误")
            print(e)

    #工具栏，点击打开主页面
    def setIndexWidget(self):
        self.cenTab.addTab(self.indexTab,QIcon(":/PIC/home.png"),"主页面")
        self.cenTab.setCurrentWidget(self.indexTab)

    #工具栏，点击打开搜索页
    def setSearchWidgetOpen(self):
        self.cenTab.addTab(self.searchTab,QIcon(":/PIC/书本查找.png"),"检索页面")
        self.cenTab.setCurrentWidget(self.searchTab)

    #工具栏，点击打开文献汇编检索
    def on_HMCSearch(self):
        self.cenTab.addTab(self.HMCTab,QIcon(":/PIC/DocumentSearch.png"),"检索-史料文献汇编")
        self.cenTab.setCurrentWidget(self.HMCTab)

    #工具栏，点击打开史料文献汇编
    def on_Catalog(self):
        self.cenTab.addTab(self.CatalogTab,QIcon(":/PIC/Catalog.png"),"浏览-史料文献汇编")
        self.cenTab.setCurrentWidget(self.CatalogTab)

    #工具栏，点击关闭所有标签
    def on_closeAllTabs(self):
        while self.cenTab.count() > 0 :
            self.cenTab.removeTab(self.cenTab.count() - 1)

    #工具栏，进入后台数据管理
    def on_setupTabs(self):
        if self.setupTab == None:
            loadSys = LoadSys(self.query)
            loadSys.Signal_CreateSetupWidget.connect(self.on_creatSetupWidget)
            loadSys.exec()
        else:
            self.cenTab.addTab(self.setupTab,"【文献数据管理】")
            self.cenTab.setCurrentWidget(self.setupTab)

    #工具栏，点击弹出关于信息窗口
    def on_About(self):
        about = AboutDialog()
        about.exec_()
    #设定标签控件的关闭事件
    def on_cenTab_close(self,index):
        self.cenTab.removeTab(index)

    #槽，设定打开四个分库
    def on_openDBView(self,int_index):
        if int_index == 1:
            DBName = "域外文献库"
            self.cenTab.addTab(self.yuwaiTab,QIcon(":/PIC/域外文献.png"), DBName)
            self.cenTab.setCurrentWidget(self.yuwaiTab)
        elif int_index == 2:
            DBName =  "档案与文物数据库"
            self.cenTab.addTab(self.danganTab,QIcon(":/PIC/档案与文物.png"), DBName)
            self.cenTab.setCurrentWidget(self.danganTab)
        elif int_index == 3:
            DBName =  "古代史料数据库"
            self.cenTab.addTab(self.gudaiTab, QIcon(":/PIC/古代史料.png"),DBName)
            self.cenTab.setCurrentWidget(self.gudaiTab)
        elif int_index == 4:
            DBName = "现代研究文献数据库"
            self.cenTab.addTab(self.xiandaiTab,QIcon(":/PIC/现代研究.png"), DBName)
            self.cenTab.setCurrentWidget(self.xiandaiTab)
        elif int_index == 5:
            self.ui.action_Catalog.triggered.emit()
        else:
            pass

    def goWhichDB(self,index):
        if index == 'XDYW':
            int_index = 4
        elif index == 'YWWX':
            int_index = 1
        elif index == 'GDSL':
            int_index = 3
        else:
            int_index = 2
        self.on_openDBView(int_index)

    #槽，打开资料的详细页面
    def on_OpenDetailView(self,md5,title,id):
        print(md5,title,id)
        #tab = RecordDetailWidget(self.DB,md5,id)
        tab = RecordDetailView(self.DB,md5,id)
        tab.Signal_RecordDetailReadPDF.connect(self.on_PDFReader)
        tab.signal_Home.connect(self.setIndexWidget)
        tab.signal_goBackDB.connect(self.goWhichDB)
        tab.signal_Query.connect(self.setSearchWidgetOpen)
        self.cenTab.addTab(tab,QIcon(":/PIC/ReadDetail.png"),title[0:12])
        self.cenTab.setCurrentWidget(tab)

    #阅读PDF
    def on_PDFReader(self,title,md5):

        bin = self.getPDFStream(md5)
        if bin != None:
            tab = WidgetPDFStream(bin,title)
            self.cenTab.addTab(tab,QIcon(":/PIC/阅读.png"),title[0:12])
            self.cenTab.setCurrentWidget(tab)
        else:
            QMessageBox.information(self,"提示","找不到文档文件。")

    #查询，辅组返回PDF流，提供阅读PDF函数使用
    def getPDFStream(self,md5):
        sqQuery = "select filebinary from infofile where md5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, md5)
        self.query.exec()
        self.query.last()
        return self.query.value("filebinary")

    def on_creatSetupWidget(self):
        self.setupTab = ManageWidget(self.DB)
        self.cenTab.addTab(self.setupTab,QIcon(":/PIC/Setup.png"), "【文献数据管理】")
        self.cenTab.setCurrentWidget(self.setupTab)

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())
