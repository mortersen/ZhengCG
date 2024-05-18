import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTableView,QMessageBox,QAbstractItemView,QTreeWidgetItem
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QFont

from UI.UI_DBTreeWidget import Ui_DBTreeView
from UI.UI_TableViewWidget import Ui_ViewDBWidget


class DBTreeWidget(QWidget):
    Signal_ViewDetailRecord = pyqtSignal(str,str,int)

    def __init__(self,DB):
        super().__init__()
        self.ui = Ui_DBTreeView()
        self.ui.setupUi(self)

        self.ui_ViewDBWidget = Ui_ViewDBWidget()
        self.detailWidget = QWidget()
        self.ui_ViewDBWidget = Ui_ViewDBWidget()
        self.ui_ViewDBWidget.setupUi(self.detailWidget)
        self.tableView = QTableView()
        self.ui_ViewDBWidget.TableLayout.addWidget(self.tableView)
        self.ui.DBLayout.addWidget(self.detailWidget)
        #按类多态生成树
        self.initTree()
        self.ui.tree.expandAll()

        self.DB = DB
        self.DB.open()
        self.sqlQuery = QSqlQuery(self.DB)
        self.qryModel = QSqlQueryModel(self)
        self.tableView.setModel(self.qryModel)

        self.currentPage = 0
        self.eachPageRecord = 20

        self.query = ''
        self.queryTotoalRecord = ''


        #树点击事件，发生查询事件，对应槽函数更新数据显示包括查询的结果和页面信息
        self.ui.tree.clicked.connect(self.updateDBView)
        self.ui_ViewDBWidget.comBox_EachPage.currentIndexChanged.connect(self.on_getEachPage)
        self.tableView.doubleClicked.connect(self.on_SendViewDetail)
        self.ui_ViewDBWidget.btn_PageUp.released.connect(self.on_PageUp)
        self.ui_ViewDBWidget.btn_PageDown.released.connect(self.on_PageDown)
        self.ui_ViewDBWidget.lineEdit_PageNum.returnPressed.connect(self.on_Goto)
        self.ui_ViewDBWidget.btn_Goto.released.connect(self.on_Goto)

    def initTree(self):
        pass

    def updateDBView(self):
        pass

    def executeQurey(self,index):
        pass
    #更新第几页和总页数
    def updateLab(self):
        self.ui_ViewDBWidget.lab_CurrentPage.setText(str(self.currentPage+1))
        self.ui_ViewDBWidget.lab_TotoalPages.setText(str(self.totoalPages))
    #计算总记录数
    def caculateTotoalRecord(self):
        try:
            self.sqlQuery.exec(self.queryTotoalRecord)
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception.__str__())
    #槽函数，响应刷新每页新的展示数
    def on_getEachPage(self):
        page = self.ui_ViewDBWidget.comBox_EachPage.currentText()
        self.eachPageRecord = int(page)
        self.currentPage = 0
        self.totoalPages = self.caculateTotoalPages()
        self.executeQurey(self.currentPage*self.eachPageRecord)
        self.updateLab()
    #计算总页数
    def caculateTotoalPages(self):
        page = self.totoalRecord // self.eachPageRecord
        if self.totoalRecord % self.eachPageRecord != 0:
            page += 1
        return page
    #执行查询
    def executeQurey(self, index):
        limit = " limit %d,%d" % (index, self.eachPageRecord)
        query = self.query + limit
        self.qryModel.setQuery(query)

    def on_PageDown(self):
        if self.currentPage + 1 < self.totoalPages:
            self.currentPage += 1
            self.executeQurey(self.currentPage*self.eachPageRecord)
            self.updateLab()

    def on_PageUp(self):

        if self.currentPage > 0:
            self.currentPage -= 1
            self.executeQurey(self.currentPage*self.eachPageRecord)
            self.updateLab()
    #跳转页
    def on_Goto(self):
        getInt = self.ui_ViewDBWidget.lineEdit_PageNum.text()
        if getInt.isdigit() :
            page = int(getInt)
            if page > 0 and page <= self.totoalPages:
                self.currentPage = page - 1
                self.executeQurey(self.currentPage*self.eachPageRecord)
                self.updateLab()
            else:
                QMessageBox.warning(self, "警告", "请检查页码范围！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"警告","请输入数字页码!",QMessageBox.Ok)
    #向主页面发射信息
    def on_SendViewDetail(self,index):
        curRec = self.qryModel.record(index.row())
        print(curRec)
        md5 = curRec.value("MD5")
        print(md5)
        title = curRec.value("TITLE")
        id = curRec.value("ID")
        print(id)
        self.Signal_ViewDetailRecord.emit(md5,title,id)

#域外文献数据库
class YWDBTreeWidget(DBTreeWidget):

    def __init__(self,DB):
        super().__init__(DB)

        self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'YWWX\'"
        self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'YWWX\'"
        # 计算总记录数
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.updateLab()

        self.tableView.setModel(self.qryModel)
        self.executeQurey(self.currentPage*self.eachPageRecord)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.verticalHeader().setDefaultSectionSize(40)
        self.tableView.setColumnWidth(0, 400)
        self.tableView.setColumnWidth(5,400)
        self.tableView.setColumnHidden(6,True)
        self.tableView.setColumnHidden(7,True)

        self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "文献来源")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "年份")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "关键字")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "内容摘要")

    def initTree(self):
        root = QTreeWidgetItem(self.ui.tree)
        item0 = QTreeWidgetItem(root)
        item1 = QTreeWidgetItem(root)
        item2 = QTreeWidgetItem(root)
        self.ui.tree.header().setVisible(False)
        self.ui.tree.setColumnHidden(1,True)
        root.setText(0,"域外文献数据库")
        root.setText(1,"0")
        font14 = QFont()
        font14.setFamily("华文楷体")
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        root.setFont(0,font14)
        item0.setText(0,"期刊")
        item0.setText(1,"1")
        item1.setText(0,"会议论文")
        item1.setText(1,"2")
        item2.setText(0,"图书")
        item2.setText(1,"3")

        font12 = QFont()
        font12.setFamily("华文楷体")
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        item0.setFont(0,font12)
        item1.setFont(0,font12)
        item2.setFont(0,font12)

    #多态，槽函数，处理选择字库操作
    def updateDBView(self):
        index = int(self.ui.tree.currentItem().text(1))
        if index == 0:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'YWWX\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'YWWX\'"
        elif index == 1:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'YWWX\' and FL2ND = \'QK\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'YWWX\'and FL2ND = \'QK\'"
        elif index == 2:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'YWWX\' and FL2ND = \'HL\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'YWWX\' AND FL2ND =\'HL\'"
        elif index == 3:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'YWWX\' and FL2ND = \'TS\'"
            self.queryTotoalRecord =  "SELECT 1 from info where FL1ST = \'YWWX\' AND FL2ND = \'TS\'"
        self.currentPage = 0
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.executeQurey(self.currentPage * self.eachPageRecord)
        self.updateLab()

#档案与文物数据库
class DADBTreeWidget(DBTreeWidget):
    def __init__(self,DB):
        super().__init__(DB)

        self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'DAWW\'"
        self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'DAWW\'"
        # 计算总记录数
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.updateLab()

        self.tableView.setModel(self.qryModel)
        self.executeQurey(self.currentPage * self.eachPageRecord)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.verticalHeader().setDefaultSectionSize(40)
        self.tableView.setColumnWidth(0, 400)
        self.tableView.setColumnWidth(5, 400)
        self.tableView.setColumnHidden(6, True)
        self.tableView.setColumnHidden(7,True)

        self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "文献来源")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "年份")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "关键字")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "内容摘要")

    def initTree(self):
        root = QTreeWidgetItem(self.ui.tree)
        item0 = QTreeWidgetItem(root)
        item1 = QTreeWidgetItem(root)
        item2 = QTreeWidgetItem(root)
        item3 = QTreeWidgetItem(root)
        self.ui.tree.header().setVisible(False)
        self.ui.tree.setColumnHidden(1,True)
        root.setText(0,"档案与文物数据库")
        root.setText(1,"0")
        font14 = QFont()
        font14.setFamily("华文楷体")
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        root.setFont(0,font14)
        item0.setText(0,"图书")
        item0.setText(1,"1")
        item1.setText(0,"期刊")
        item1.setText(1,"2")
        item2.setText(0,"报纸")
        item2.setText(1,"3")
        item2.setText(0, "会议论文")
        item2.setText(1, "4")

        font12 = QFont()
        font12.setFamily("华文楷体")
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        item0.setFont(0,font12)
        item1.setFont(0,font12)
        item2.setFont(0,font12)
        item3.setFont(0,font12)

    # 多态，槽函数，处理选择字库操作
    def updateDBView(self):
        index = int(self.ui.tree.currentItem().text(1))
        if index == 0:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'DAWW\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'DAWW\'"
        elif index == 1:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'DAWW\' and FL2ND = \'TS\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'YWWX\'and FL2ND = \'TS\'"
        elif index == 2:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'DAWW\' and FL2ND = \'QK\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'DAWW\' AND FL2ND =\'QK\'"
        elif index == 3:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'DAWW\' and FL2ND = \'BZ\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'DAWW\' AND FL2ND = \'BZ\'"
        elif index == 4:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'DAWW\' and FL2ND = \'HL\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'DAWW\' AND FL2ND = \'HL\'"
        self.currentPage = 0
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.executeQurey(self.currentPage * self.eachPageRecord)
        self.updateLab()

#古代史料数据库
class GDDBTreeWidget(DBTreeWidget):
    def __init__(self, DB):
        super().__init__(DB)

        self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\'"
        self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\'"
        # 计算总记录数
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.updateLab()

        self.tableView.setModel(self.qryModel)
        self.executeQurey(self.currentPage * self.eachPageRecord)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.verticalHeader().setDefaultSectionSize(40)
        self.tableView.setColumnWidth(0, 400)
        self.tableView.setColumnWidth(7, 400)
        self.tableView.setColumnHidden(8, True)
        self.tableView.setColumnHidden(9,True)

        self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "文献来源")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "丛书名")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "卷")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "册")
        self.qryModel.setHeaderData(6, Qt.Horizontal, "关键字")
        self.qryModel.setHeaderData(7, Qt.Horizontal, "内容摘要")

    def initTree(self):
        root = QTreeWidgetItem(self.ui.tree)
        item0 = QTreeWidgetItem(root)
        item1 = QTreeWidgetItem(root)
        item0_ZS = QTreeWidgetItem(item0)
        item0_BNS = QTreeWidgetItem(item0)
        item0_DZL = QTreeWidgetItem(item0)
        item0_BJSW = QTreeWidgetItem(item0)
        item0_MJWX = QTreeWidgetItem(item0)
        item0_QT = QTreeWidgetItem(item0)
        self.ui.tree.header().setVisible(False)
        self.ui.tree.setColumnHidden(1, True)
        root.setText(0, "古代史料数据库")
        root.setText(1, "0")
        font14 = QFont()
        font14.setFamily("华文楷体")
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        root.setFont(0, font14)

        item0.setText(0, "图书")
        item0.setText(1, "1")
        item1.setText(0, "期刊")
        item1.setText(1, "2")

        item0_ZS.setText(0, "正史类")
        item0_ZS.setText(1, "3")
        item0_BNS.setText(0, "编年史类")
        item0_BNS.setText(1, "4")
        item0_DZL.setText(0, "地志类")
        item0_DZL.setText(1, "5")
        item0_BJSW.setText(0, "笔记诗文集类")
        item0_BJSW.setText(1, "6")
        item0_MJWX.setText(0, "民间文献类")
        item0_MJWX.setText(1, "7")
        item0_QT.setText(0, "其他")
        item0_QT.setText(1, "8")

        font12 = QFont()
        font12.setFamily("华文楷体")
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        item0.setFont(0, font12)
        item1.setFont(0, font12)

        item0_ZS.setFont(0,font12)
        item0_BNS.setFont(0, font12)
        item0_DZL.setFont(0, font12)
        item0_BJSW.setFont(0, font12)
        item0_MJWX.setFont(0, font12)
        item0_QT.setFont(0, font12)


    # 多态，槽函数，处理选择字库操作
    def updateDBView(self):
            index = int(self.ui.tree.currentItem().text(1))
            if index == 0:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\'"
            elif index == 1:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' and FL2ND = \'TS\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\'and FL2ND = \'TS\'"
            elif index == 2:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' and FL2ND = \'QK\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'QK\'"
            elif index == 3:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'ZS\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'ZS\'"
            elif index == 4:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'BNS\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'BNS\'"
            elif index == 5:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'DZL\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'DZL\'"
            elif index == 6:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'BJSW\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'BJSW\'"
            elif index == 7:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'MJWX\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'MJWX\'"
            elif index == 8:
                self.query = "SELECT Title,author,Source,series,volumn,periods,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'QT\'"
                self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'GDSL\' AND FL2ND =\'TS\' AND FL3RD =\'QT\'"
            self.currentPage = 0
            self.totoalRecord = self.caculateTotoalRecord()
            self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
            self.totoalPages = self.caculateTotoalPages()
            self.executeQurey(self.currentPage * self.eachPageRecord)
            self.updateLab()


#现代研究文献数据库
class XDDBTreeWidget(DBTreeWidget):
    def __init__(self, DB):
        super().__init__(DB)

        self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\'"
        self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\'"
        # 计算总记录数
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.updateLab()

        self.tableView.setModel(self.qryModel)
        self.executeQurey(self.currentPage * self.eachPageRecord)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.verticalHeader().setDefaultSectionSize(40)
        self.tableView.setColumnWidth(0, 400)
        self.tableView.setColumnWidth(5, 400)
        self.tableView.setColumnHidden(6, True)
        self.tableView.setColumnHidden(7,True)

        self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "文献来源")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "年份")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "关键字")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "内容摘要")
    def initTree(self):
        root = QTreeWidgetItem(self.ui.tree)
        item0 = QTreeWidgetItem(root)
        item1 = QTreeWidgetItem(root)
        item2 = QTreeWidgetItem(root)
        item3 = QTreeWidgetItem(root)
        item4 = QTreeWidgetItem(root)
        item5 = QTreeWidgetItem(root)
        item6 = QTreeWidgetItem(root)
        self.ui.tree.header().setVisible(False)
        self.ui.tree.setColumnHidden(1, True)
        root.setText(0, "现代研究文献数据库")
        root.setText(1, "0")
        font14 = QFont()
        font14.setFamily("华文楷体")
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        root.setFont(0, font14)
        item0.setText(0, "图书")
        item0.setText(1, "1")
        item1.setText(0, "期刊")
        item1.setText(1, "2")
        item2.setText(0, "学位论文")
        item2.setText(1, "3")
        item3.setText(0, "会议论文")
        item3.setText(1, "4")
        item4.setText(0,"报纸")
        item4.setText(1,"5")
        item5.setText(0,"外国学者研究")
        item5.setText(1,"6")
        item6.setText(0,"调研报告")
        item6.setText(1,"7")


        font12 = QFont()
        font12.setFamily("华文楷体")
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        item0.setFont(0, font12)
        item1.setFont(0, font12)
        item2.setFont(0, font12)
        item3.setFont(0, font12)
        item4.setFont(0, font12)
        item5.setFont(0, font12)
        item6.setFont(0, font12)

    # 多态，槽函数，处理选择字库操作
    def updateDBView(self):
        index = int(self.ui.tree.currentItem().text(1))
        if index == 0:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\'"
        elif index == 1:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'TS\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\'and FL2ND = \'TS\'"
        elif index == 2:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'QK\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\' AND FL2ND =\'QK\'"
        elif index == 3:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'XL\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\' AND FL2ND = \'XL\'"
        elif index == 4:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'HL\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\' AND FL2ND = \'HL\'"
        elif index == 5:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'BZ\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\' AND FL2ND = \'BZ\'"
        elif index == 6:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'WY\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\' AND FL2ND = \'WY\'"
        elif index == 7:
            self.query = "SELECT Title,author,Source,year,keywords,abstract,md5,id FROM INFO WHERE FL1ST = \'XDYW\' and FL2ND = \'YB\'"
            self.queryTotoalRecord = "SELECT 1 from info where FL1ST = \'XDYW\' AND FL2ND = \'YB\'"
        self.currentPage = 0
        self.totoalRecord = self.caculateTotoalRecord()
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totoalRecord))
        self.totoalPages = self.caculateTotoalPages()
        self.executeQurey(self.currentPage * self.eachPageRecord)
        self.updateLab()


if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = DBTreeWidget()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())