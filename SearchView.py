import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTableView,QMessageBox,QAbstractItemView
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from PyQt5.QtCore import Qt,pyqtSignal

from UI.UI_SearchWidget import Ui_searchWidget
from UI.UI_TableViewWidget import Ui_ViewDBWidget


viewName =['BookView','PeriodView','NewspaperView','ThesisView','ConferencePaperView','ReportView','InfoView']

#搜索页类
class SearchWidget(QWidget):
    SignalViewDetailRecord = pyqtSignal(str,str,int)
    def __init__(self,DB):
        super().__init__()
        self.ui = Ui_searchWidget()
        self.ui.setupUi(self)

        self.DB = DB
        self.DB.open()
        self.sqlQuery = QSqlQuery(self.DB)
        self.qryModel = QSqlQueryModel(self)

        self.tableView = QTableView()
        self.tableView.setModel(self.qryModel)

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.verticalHeader().setDefaultSectionSize(40)
        self.tableView.setColumnWidth(0, 400)


        #装饰数据库查询的结果显示页面
        self.viewDBWidget = QWidget()
        self.ui_ViewDBWidget = Ui_ViewDBWidget()
        self.ui_ViewDBWidget.setupUi(self.viewDBWidget)
        self.ui_ViewDBWidget.TableLayout.addWidget(self.tableView)

        #将结果显示页面装入搜索页面中
        self.ui.TableViewLayout.addWidget(self.viewDBWidget)

        #设置初始的一些参数
        #检索库，默认0-图书,1-期刊，2-报纸，3-论文，4-会议议论，5-调研报告
        self.indexView = 0
        self.notInSubDB = ''
        self.condition = ''
        self.currentPage = 0
        self.eachPageRecord = 20
        self.totalRecord = 0
        self.totalPages = 0
        self.query = ''

        #c初始化显示内容
        self.ui_ViewDBWidget.lab_CurrentPage.setText('1')
        self.ui_ViewDBWidget.lab_TotoalRecord.setText('1')
        self.ui_ViewDBWidget.lab_TotoalPages.setText('1')


        #控件信号
        self.ui.comBox_WhatkindSearchFor.currentIndexChanged.connect(self.on_comBoxWhichView)
        self.ui_ViewDBWidget.comBox_EachPage.currentIndexChanged.connect(self.on_comBoxEachPage)
        self.ui.checkBox_YUWAI.stateChanged.connect(self.on_checkNotInSubDB)
        self.ui.checkBox_XIANDAI.stateChanged.connect(self.on_checkNotInSubDB)
        self.ui.checkBox_GUSHI.stateChanged.connect(self.on_checkNotInSubDB)
        self.ui.checkBox_DANGAN.stateChanged.connect(self.on_checkNotInSubDB)
        self.ui.lineEdit_WhatSearch.returnPressed.connect(self.on_SearchFor)
        self.ui.btn_Search.released.connect(self.on_SearchFor)
        self.ui_ViewDBWidget.btn_PageDown.released.connect(self.on_btnPageDown)
        self.ui_ViewDBWidget.btn_PageUp.released.connect(self.on_btnPageUp)
        self.ui_ViewDBWidget.btn_Goto.released.connect(self.on_btnGoto)
        self.ui_ViewDBWidget.lineEdit_PageNum.returnPressed.connect(self.on_btnGoto)
        self.tableView.doubleClicked.connect(self.on_DoubleClicked)

        self.ui.btn_allDB.released.connect(self.on_QueryAllDB)
        self.ui.btn_bookDB.released.connect(self.on_QueryBookDB)
        self.ui.btn_periodDB.released.connect(self.on_QueryPeriodDB)
        self.ui.btn_conferencePaperDB.released.connect(self.on_QueryConferencePaperDB)
        self.ui.btn_ThesisDB.released.connect(self.on_QueryThesisDB)
        self.ui.btn_reportDB.released.connect(self.on_QueryReportDB)
        self.ui.btn_newsPaparDB.released.connect(self.on_QueryNewspaperDB)

    def on_QueryAllDB(self):
        self.condition = "1"
        self.indexView = 6
        self.on_QueryFLDB(0)

    def on_QueryBookDB(self):
        self.condition = "1"
        self.indexView = 0
        self.on_QueryFLDB(0)
    def on_QueryPeriodDB(self):
        self.condition = "1"
        self.indexView = 1
        self.on_QueryFLDB(0)
    def on_QueryConferencePaperDB(self):
        self.condition = "1"
        self.indexView = 4
        self.on_QueryFLDB(0)
    def on_QueryThesisDB(self):
        self.condition = "1"
        self.indexView = 3
        self.on_QueryFLDB(0)
    def on_QueryReportDB(self):
        self.condition = "1"
        self.indexView = 5
        self.on_QueryFLDB(0)
    def on_QueryNewspaperDB(self):
        self.condition = "1"
        self.indexView = 2
        self.on_QueryFLDB(0)

    def on_QueryFLDB(self,index):
        try:
            self.executeQuery(index)
            self.updateRecordsAndPages()
            self.ui_ViewDBWidget.lab_CurrentPage.setText('1')
            self.setColumnHide()
            self.setColumnTitle()
        except Exception:
            print(Exception.__str__())

    #获取用户的检索范围
    def on_checkNotInSubDB(self):
        self.notInSubDB = ''
        if self.ui.checkBox_DANGAN.isChecked() == False:
            self.notInSubDB = 'FL1ST != \'DAWW\''
        if self.ui.checkBox_GUSHI.isChecked() == False:
            if self.notInSubDB.__len__() != 0 :
                self.notInSubDB += ' AND FL1ST != \'GDSL\''
            else:
                self.notInSubDB = 'FL1ST != \'GDSL\''
        if self.ui.checkBox_XIANDAI.isChecked() == False:
            if self.notInSubDB.__len__() != 0 :
                self.notInSubDB += ' AND FL1ST != \'XDYW\''
            else:
                self.notInSubDB = 'FL1ST != \'XDYW\''
        if self.ui.checkBox_YUWAI.isChecked() == False:
            if self.notInSubDB.__len__() != 0 :
                self.notInSubDB += ' AND FL1ST != \'YWWX\''
            else:
                self.notInSubDB = 'FL1ST != \'WYWX\''
        #print(self.notInSubDB)

    #槽函数
    #执行查找
    def on_SearchFor(self):
        try:
            keyWords = self.ui.lineEdit_WhatSearch.text().strip()
            if keyWords.__len__() == 0:
                self.condition = ''
                QMessageBox.information(self, "提示！", '请在输入框内填写检索的关键字词。', QMessageBox.Ok)
            else:
                self.condition = "TITLE LIKE \'%%%s%%\' or KEYWORDS LIKE \'%%%s%%\' or ABSTRACT LIKE \'%%%s%%\' or AUTHOR LIKE \'%%%s%%\'" % (keyWords, keyWords, keyWords,keyWords)
                self.executeQuery(0)
                self.updateRecordsAndPages()
                self.ui_ViewDBWidget.lab_CurrentPage.setText('1')
                self.setColumnHide()
                self.setColumnTitle()
        except Exception:
            print(Exception.__str__())

    #双击事件
    def on_DoubleClicked(self,index):
        curRec = self.qryModel.record(index.row())
        md5 = curRec.value("MD5")
        print(md5)
        title = curRec.value("TITLE")
        id = curRec.value("ID")
        print(id)
        self.SignalViewDetailRecord.emit(md5,title,id)



    #下拉框，选择检索的数据库
    def on_comBoxWhichView(self):
        self.indexView = self.ui.comBox_WhatkindSearchFor.currentIndex()
        #print(viewName[self.indexView])

    #执行查找,并回到第一页
    def executeQuery(self,index):
        try:
            #在四个一级分类库中查找
            if self.notInSubDB == '':
                self.query = "select * from %s where %s limit %d,%d" % (viewName[self.indexView],self.condition,index,self.eachPageRecord)
            else:
                self.query = "select * from %s where (%s) and (%s) limit %d,%d" % (viewName[self.indexView],self.condition,self.notInSubDB,index,self.eachPageRecord)
            #print(self.query)
            self.qryModel.setQuery(self.query)
            self.tableView.setColumnWidth(0,400)
        except Exception:
            print(Exception.__str__())

    def setColumnTitle(self):
        if self.indexView == 0:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "出版社")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "总页数")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "关键字")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "丛书系列")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "出版年份")
            self.qryModel.setHeaderData(6, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(7, Qt.Horizontal, "内容简介")
            self.tableView.setColumnHidden(8,True)
            self.tableView.setColumnHidden(9, True)
            self.tableView.setColumnHidden(10, True)
        elif self.indexView == 1:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "作者单位")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "期刊")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "页码范围")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "页数")
            self.qryModel.setHeaderData(6, Qt.Horizontal, "年份")
            self.qryModel.setHeaderData(7, Qt.Horizontal, "期号")
            self.qryModel.setHeaderData(8, Qt.Horizontal, "卷")
            self.qryModel.setHeaderData(9, Qt.Horizontal, "关键字")
            self.qryModel.setHeaderData(10, Qt.Horizontal, "摘要")
            self.tableView.setColumnHidden(11, True)
            self.tableView.setColumnHidden(12, True)
            self.tableView.setColumnHidden(13, True)
        elif self.indexView == 2:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "作者单位")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "年份")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "报纸")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "关键字")
            self.qryModel.setHeaderData(6, Qt.Horizontal, "主要内容")
            self.tableView.setColumnHidden(7, True)
            self.tableView.setColumnHidden(8, True)
            self.tableView.setColumnHidden(9, True)
        elif self.indexView == 3:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "题目")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "作者单位")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "导师")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "关键字")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "摘要")
            self.qryModel.setHeaderData(6, Qt.Horizontal, "年份")
            self.tableView.setColumnHidden(7, True)
            self.tableView.setColumnHidden(8, True)
            self.tableView.setColumnHidden(9, True)
        elif self.indexView == 4:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "议题")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "会议地址")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "年份")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "关键字")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "议题简介")
            self.tableView.setColumnHidden(6, True)
            self.tableView.setColumnHidden(7, True)
            self.tableView.setColumnHidden(8, True)
        elif self.indexView == 5:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "题目")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "作者单位")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "年份")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "关键字")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "报告主旨")
            self.tableView.setColumnHidden(6, True)
            self.tableView.setColumnHidden(7, True)
            self.tableView.setColumnHidden(8, True)
        else:
            self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
            self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
            self.qryModel.setHeaderData(2, Qt.Horizontal, "作者单位")
            self.qryModel.setHeaderData(3, Qt.Horizontal, "文献来源")
            self.qryModel.setHeaderData(4, Qt.Horizontal, "年份")
            self.qryModel.setHeaderData(5, Qt.Horizontal, "丛书名称")
            self.qryModel.setHeaderData(6, Qt.Horizontal, "会议地点")
            self.qryModel.setHeaderData(7, Qt.Horizontal, "导师")
            self.qryModel.setHeaderData(8, Qt.Horizontal, "关键词")
            self.qryModel.setHeaderData(9, Qt.Horizontal, "内容摘要")
            self.qryModel.setHeaderData(10, Qt.Horizontal, "卷号")
            self.qryModel.setHeaderData(11, Qt.Horizontal, "期号")
            self.qryModel.setHeaderData(12, Qt.Horizontal, "页码范围")
            self.qryModel.setHeaderData(13, Qt.Horizontal, "页数")
            self.tableView.setColumnHidden(14, True)
            self.tableView.setColumnHidden(15, True)
            self.tableView.setColumnHidden(16, True)

    def setColumnHide(self):
            self.tableView.setColumnHidden(6,False)
            self.tableView.setColumnHidden(7,False)
            self.tableView.setColumnHidden(8,False)
            self.tableView.setColumnHidden(9,False)
            self.tableView.setColumnHidden(11,False)
            self.tableView.setColumnHidden(12,False)
            self.tableView.setColumnHidden(13, True)
            self.tableView.setColumnHidden(14, True)
            self.tableView.setColumnHidden(15, True)
            self.tableView.setColumnHidden(16, True)



    #获取每页展示几条记录
    def on_comBoxEachPage(self):
        page = self.ui_ViewDBWidget.comBox_EachPage.currentText()
        self.eachPageRecord = int(page)
        self.currentPage = 0
        self.executeQuery(self.currentPage)
        self.ui_ViewDBWidget.lab_CurrentPage.setText('1')
        self.updateRecordsAndPages()

    #下一页
    def on_btnPageDown(self):
        if self.currentPage + 1 < self.totalPages:
            self.currentPage += 1
            self.executeQuery(self.currentPage*self.eachPageRecord)
            self.ui_ViewDBWidget.lab_CurrentPage.setText(str(self.currentPage+1))

    #上一页
    def on_btnPageUp(self):
        if self.currentPage - 1 >= 0 :
            self.currentPage -= 1
            self.executeQuery(self.currentPage * self.eachPageRecord)
            self.ui_ViewDBWidget.lab_CurrentPage.setText(str(self.currentPage+1))

     #获取总记录数

    #页面跳转
    def on_btnGoto(self):
        try:
            if self.ui_ViewDBWidget.lineEdit_PageNum.text().isdigit() :
                pageNum = int(self.ui_ViewDBWidget.lineEdit_PageNum.text())
                if pageNum >0 and pageNum<=self.totalPages:
                    self.currentPage = pageNum -1
                    self.executeQuery(self.currentPage * self.eachPageRecord)
                    self.ui_ViewDBWidget.lab_CurrentPage.setText(str(self.currentPage + 1))
                else:
                    QMessageBox.warning(self, "警告", "请输入正确页码范围", QMessageBox.Ok)
            else:
                QMessageBox.warning(self,"警告","请输入数字页码",QMessageBox.Ok)
        except Exception:
            print(Exception.__str__())

    #计算总记录数
    def getTotalRecord(self):
        try:
            if self.notInSubDB == '':
                query = "select * from %s where %s" % (viewName[self.indexView],self.condition)
            else:
                query = "select * from %s where (%s) and (%s)" % (viewName[self.indexView],self.condition,self.notInSubDB)
            self.sqlQuery.exec(query)
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception)

    #更新总记录数，总页码数
    def updateRecordsAndPages(self):
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.totalRecord // self.eachPageRecord
        if self.totalRecord % self.eachPageRecord != 0:
            self.totalPages += 1
        self.ui_ViewDBWidget.lab_TotoalPages.setText(str(self.totalPages))
        self.ui_ViewDBWidget.lab_TotoalRecord.setText(str(self.totalRecord))


if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWindow = SearchWidget()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())
