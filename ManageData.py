import hashlib,os
from PyQt5.QtWidgets import QWidget,QDataWidgetMapper,QAbstractItemView,QMessageBox,QDialog,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel,QSqlRecord
import sqlite3
from UI.UI_DetailWidget import Ui_DetailWidget
from UI.UI_ManageWidget import Ui_ManageWidget
from UI.UI_InsertDetailWidget import Ui_InsertDetailWidget

#添加文档
class InsertDetailWidget(QDialog):
    def __init__(self,sqlQuery=QSqlQuery):
        super().__init__()
        self.ui = Ui_InsertDetailWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("添加文档资料")
        self.sqlQuery = sqlQuery

        self.conn = sqlite3.connect("DB/ZhengCG.db")
        self.cur = self.conn.cursor()

        self.ui.btn_Save.released.connect(self.onSaveData)
        self.ui.btn_Reflesh.released.connect(self.onRefleshData)
        self.ui.btn_File.released.connect(self.onChooseFile)

    def onChooseFile(self):
        fileName,fileType = QFileDialog.getOpenFileName(self,"选取文件",os.getcwd(),"(*.pdf)")
        if fileName != '':
            self.ui.label_File.setText(fileName)
        return
    #刷新文档的数据
    def onRefleshData(self):
        self.clearData()

    def onSaveData(self):
        try:
            title = self.ui.lineEdit_Title.text()
            if title == "":
                self.ui.lineEdit_Title.setFocus()
                return
            author = self.ui.lineEdit_Author.text()
            if author == "":
                self.ui.lineEdit_Author.setFocus()
                return
            source = self.ui.lineEdit_Source.text()
            year = self.ui.lineEdit_Year.text()
            keywords = self.ui.lineEdit_Keywords.text()
            abstract = self.ui.textEdit_Abstract.toPlainText()
            pages = self.ui.lineEdit_Pages.text()
            atpage = self.ui.lineEdit_Atpage.text()
            volumn = self.ui.lineEdit_Volumn.text()
            period = self.ui.lineEdit_Periods.text()
            authorUnit = self.ui.lineEdit_AuthorUnit.text()
            series = self.ui.lineEdit_Series.text()
            venue = self.ui.lineEdit_Venue.text()
            teacher = self.ui.lineEdit_Teacher.text()
            f1 = self.getDB(self.ui.comboBox_DB.currentIndex())
            f2 = self.getFL(self.ui.comboBox_FL.currentIndex())
            md5 = None
            #当有添加文档文件时
            fileUrl = self.ui.label_File.text()
            if fileUrl !="" :
                filePDF = open(fileUrl, "rb")
                fileBinary = filePDF.read()
                md5 = (hashlib.md5(fileBinary).hexdigest())
                filePDF.close()
                self.cur.execute("INSERT INTO INFOFILE VALUES(?,?,?)",(None,md5,fileBinary))
                self.conn.commit()
            self.sqlQuery.prepare("INSERT INTO INFO (TITLE,AUTHOR,SOURCE,YEAR,KEYWORDS,ABSTRACT,FL1ST,FL2ND,PAGES,ATPAGE,VOLUMN,PERIODS,AUTHORUNIT,SERIES,VENUE,TEACHER,MD5) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            self.sqlQuery.addBindValue(title)
            self.sqlQuery.addBindValue(author)
            self.sqlQuery.addBindValue(source)
            self.sqlQuery.addBindValue(year)
            self.sqlQuery.addBindValue(keywords)
            self.sqlQuery.addBindValue(abstract)
            self.sqlQuery.addBindValue(f1)
            self.sqlQuery.addBindValue(f2)
            self.sqlQuery.addBindValue(pages)
            self.sqlQuery.addBindValue(atpage)
            self.sqlQuery.addBindValue(volumn)
            self.sqlQuery.addBindValue(period)
            self.sqlQuery.addBindValue(authorUnit)
            self.sqlQuery.addBindValue(series)
            self.sqlQuery.addBindValue(venue)
            self.sqlQuery.addBindValue(teacher)
            self.sqlQuery.addBindValue(md5)
            self.sqlQuery.exec()
            QMessageBox.information(self,"提示","添加成功！",QMessageBox.Ok)
            self.clearData()
        except Exception:
            print(Exception.__str__())

    def getDB(self,index):
        if index == 0:
            return "DAWW"
        if index == 1:
            return "GDSL"
        if index == 2:
            return "YWWX"
        if index == 3:
            return "XDYW"

    def getFL(self,index):
        if index == 0:
            return "TS"
        if index == 1:
            return "QK"
        if index == 2:
            return "BZ"
        if index == 3:
            return "XL"
        if index == 4:
            return "HL"
        if index == 5:
            return "YB"
        if index == 6:
            return "WY"

    #填写数据清空
    def clearData(self):
        self.ui.lineEdit_Title.clear()
        self.ui.lineEdit_Author.clear()
        self.ui.lineEdit_Source.clear()
        self.ui.lineEdit_Keywords.clear()
        self.ui.lineEdit_Pages.clear()
        self.ui.lineEdit_Atpage.clear()
        self.ui.lineEdit_Volumn.clear()
        self.ui.lineEdit_Periods.clear()
        self.ui.lineEdit_AuthorUnit.clear()
        self.ui.lineEdit_Series.clear()
        self.ui.lineEdit_Venue.clear()
        self.ui.lineEdit_Teacher.clear()
        self.ui.textEdit_Abstract.clear()
        self.ui.label_File.clear()
        self.ui.comboBox_FL.setCurrentIndex(0)
        self.ui.comboBox_DB.setCurrentIndex(0)

#修改文档
class UpdateDetailWidget(QDialog):
    def __init__(self,sqlQuery=QSqlQuery,curRec=QSqlRecord):
        super().__init__()
        self.ui = Ui_InsertDetailWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("编辑文档信息")
        self.sqlQuery = sqlQuery
        self.curRec = curRec

        self.ui.btn_Reflesh.released.connect(self.setUpdateRecord)
        self.ui.btn_Save.released.connect(self.onUpdateRecord)

        self.setUpdateRecord()

    #载入原记录信息
    def setUpdateRecord(self):
        self.ui.lineEdit_Title.setText(self.curRec.value("TITLE"))
        self.ui.lineEdit_Author.setText(self.curRec.value("AUTHOR"))
        self.ui.lineEdit_Year.setText(self.curRec.value("YEAR"))
        self.ui.lineEdit_Teacher.setText(self.curRec.value("TEACHER"))
        self.ui.lineEdit_Series.setText(self.curRec.value("SERIES"))
        self.ui.lineEdit_Source.setText(self.curRec.value("SOURCE"))
        self.ui.lineEdit_AuthorUnit.setText(self.curRec.value("AUTHORUNIT"))
        self.ui.lineEdit_Venue.setText(self.curRec.value("VENUE"))
        self.ui.lineEdit_Periods.setText(self.curRec.value("PERIODS"))
        self.ui.lineEdit_Volumn.setText(self.curRec.value("VOLUMN"))
        self.ui.lineEdit_Pages.setText(self.curRec.value("PAGES"))
        self.ui.lineEdit_Atpage.setText(self.curRec.value("ATPAGE"))
        self.ui.lineEdit_Keywords.setText(self.curRec.value("KEYWORDS"))
        self.ui.textEdit_Abstract.setText(self.curRec.value("ABSTRACT"))
        self.ui.comboBox_DB.setCurrentIndex(self.getDBIndex((self.curRec.value("FL1ST"))))
        self.ui.comboBox_FL.setCurrentIndex(self.getFLIndex((self.curRec.value("FL2ND"))))
        self.ui.label_File.setText(self.curRec.value("MD5"))
    #更新记录信息
    def onUpdateRecord(self):
        try:
            title = self.ui.lineEdit_Title.text()
            if title == "":
                self.ui.lineEdit_Title.setFocus()
                return
            author = self.ui.lineEdit_Author.text()
            if author == "":
                self.ui.lineEdit_Author.setFocus()
                return
            source = self.ui.lineEdit_Source.text()
            year = self.ui.lineEdit_Year.text()
            keywords = self.ui.lineEdit_Keywords.text()
            abstract = self.ui.textEdit_Abstract.toPlainText()
            pages = self.ui.lineEdit_Pages.text()
            atpage = self.ui.lineEdit_Atpage.text()
            volumn = self.ui.lineEdit_Volumn.text()
            period = self.ui.lineEdit_Periods.text()
            authorUnit = self.ui.lineEdit_AuthorUnit.text()
            series = self.ui.lineEdit_Series.text()
            venue = self.ui.lineEdit_Venue.text()
            teacher = self.ui.lineEdit_Teacher.text()
            f1 = self.getDB(self.ui.comboBox_DB.currentIndex())
            f2 = self.getFL(self.ui.comboBox_FL.currentIndex())
            #md5 = None
            self.sqlQuery.prepare("INSERT INTO INFO (TITLE,AUTHOR,SOURCE,YEAR,KEYWORDS,ABSTRACT,FL1ST,FL2ND,PAGES,ATPAGE,VOLUMN,PERIODS,AUTHORUNIT,SERIES,VENUE,TEACHER) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            self.sqlQuery.addBindValue(title)
            self.sqlQuery.addBindValue(author)
            self.sqlQuery.addBindValue(source)
            self.sqlQuery.addBindValue(year)
            self.sqlQuery.addBindValue(keywords)
            self.sqlQuery.addBindValue(abstract)
            self.sqlQuery.addBindValue(f1)
            self.sqlQuery.addBindValue(f2)
            self.sqlQuery.addBindValue(pages)
            self.sqlQuery.addBindValue(atpage)
            self.sqlQuery.addBindValue(volumn)
            self.sqlQuery.addBindValue(period)
            self.sqlQuery.addBindValue(authorUnit)
            self.sqlQuery.addBindValue(series)
            self.sqlQuery.addBindValue(venue)
            self.sqlQuery.addBindValue(teacher)
            #self.sqlQuery.addBindValue(md5)
            self.sqlQuery.exec()
            QMessageBox.information(self,"提示","修改数据成功！",QMessageBox.Ok)
        except Exception:
            print(Exception.__str__())

    def getDB(self, index):
        if index == 0:
            return "DAWW"
        if index == 1:
            return "GDSL"
        if index == 2:
            return "YWWX"
        if index == 3:
            return "XDYW"

    def getFL(self, index):
        if index == 0:
            return "TS"
        if index == 1:
            return "QK"
        if index == 2:
            return "BZ"
        if index == 3:
            return "XL"
        if index == 4:
            return "HL"
        if index == 5:
            return "YB"
        if index == 6:
            return "WY"

    def getFLIndex(self, f2):
        if f2 == 'TS':
            return 0
        if f2 == 'QK':
            return 1
        if f2 == 'BZ':
            return 2
        if f2 == 'XL':
            return 3
        if f2 == 'HL':
            return 4
        if f2 == 'YB':
            return 5
        if f2 == 'WY':
            return 6

    def getDBIndex(self, f1):
        if f1 == 'DAWW':
            return 0
        if f1 == 'GDSL':
            return 1
        if f1 == 'YWWX':
            return 2
        if f1 == 'XDYW':
            return 3
        return -1


class DetailWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DetailWidget()
        self.ui.setupUi(self)

class ManageWidget(QWidget):

    def __init__(self,DB):
        super().__init__()
        self.ui = Ui_ManageWidget()
        self.ui.setupUi(self)

        self.detailWidget= DetailWidget()
        self.ui.Layout_Detail.addWidget(self.detailWidget)

        #事件-槽
        self.ui.btn_Query.released.connect(self.onQuery)
        self.ui.btn_Reload.released.connect(self.onRefresh)
        self.ui.comboBox_EachPageRecord.currentIndexChanged.connect(self.oneachPageRecord)
        self.ui.btn_PageUp.released.connect(self.onPageUp)
        self.ui.btn_PageDown.released.connect(self.onPageDown)
        self.ui.btn_Goto.released.connect(self.onGotoPage)
        self.ui.lineEdit_SearchContext.returnPressed.connect(self.onQuery)
        self.ui.lineEdit_TargetPage.returnPressed.connect(self.onGotoPage)
        self.ui.btn_InsertData.released.connect(self.onInsertData)
        self.ui.btn_Delete.released.connect(self.onDelete)
        self.ui.btn_Update.released.connect(self.onUpdata)

        self.DB = DB
        self.DB.open()
        self.sqlQuery = QSqlQuery(self.DB)
        self.queryModel = QSqlQueryModel(self)
        self.mapper = QDataWidgetMapper(self)
        self.ui.tableView.setModel(self.queryModel)

        # 获取默认选择模型
        self.selectionModel = self.ui.tableView.selectionModel()
        self.selectionModel.currentRowChanged.connect(self.do_currentRowChanged)
        # 设置表格样式
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(40)

        #初始化页面标签
        self.currentPage = 0
        self.eachPageRecord = 20
        self.totalRecord = self.getTotalRecord()
        self.totalPages = self.caculateTotoalPage()
        self.updateLable()
        self.ui.label_TotalRecord.setText("共收录文档"+str(self.totalRecord)+"条")

        #初始化条件查询
        self.condition = ""

        #执行第一次查询
        self.executeQuery(0)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.ui.tableView.setColumnWidth(0, 400)
        self.queryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "文献出处")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "年份")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "关键字词")
        self.ui.tableView.setColumnWidth(4, 200)
        self.queryModel.setHeaderData(5, Qt.Horizontal, "主要内容")
        self.ui.tableView.setColumnWidth(5, 600)
        #隐藏不显示
        self.ui.tableView.setColumnHidden(6, True)
        self.ui.tableView.setColumnHidden(7, True)
        self.ui.tableView.setColumnHidden(8, True)
        self.ui.tableView.setColumnHidden(9, True)
        self.ui.tableView.setColumnHidden(10, True)
        self.ui.tableView.setColumnHidden(11, True)
        self.ui.tableView.setColumnHidden(12, True)
        self.ui.tableView.setColumnHidden(13, True)
        self.ui.tableView.setColumnHidden(14, True)
        self.ui.tableView.setColumnHidden(15, True)
        self.ui.tableView.setColumnHidden(16, True)
        self.ui.tableView.setColumnHidden(17,True)
        #映射至文献详细界面
        self.mapper.setModel(self.queryModel)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Title, 0)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Author, 1)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Source, 2)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Source, 3)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Keywords, 4)
        self.mapper.addMapping(self.detailWidget.ui.textEdit_Abstract, 5)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Pages, 8)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_AtPage, 9)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Volumn, 10)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Periods, 11)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_AuthorUnit, 12)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Series, 13)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Venue, 14)
        self.mapper.addMapping(self.detailWidget.ui.lineEdit_Teacher, 15)
        self.mapper.toFirst()
    #槽，触发鼠标选择行事件，显示当前行的详细信息到文献详细页面
    def do_currentRowChanged(self,current,previous):
        curRec = self.queryModel.record(current.row())
        self.detailWidget.ui.comboBox_DB.setCurrentIndex(self.getDBIndex(curRec.value("FL1ST")))
        self.detailWidget.ui.comboBox_FL.setCurrentIndex((self.getFLIndex(curRec.value("FL2ND"))))
        self.mapper.setCurrentIndex(current.row())

    #获取总记录数
    def getTotalRecord(self):
        try:
            self.sqlQuery.exec("select 1 from Info")
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception)
    #计算查询的总记录
    def caculateConditionRecord(self):
        try:
            query = "select 1 from info where %s" % self.condition
            self.sqlQuery.exec(query)
            self.sqlQuery.last()
            self.totalRecord = self.sqlQuery.at() + 1
            if self.totalRecord > 0:
                self.ui.label_QueryResuat.setText("共查询" + str(self.totalRecord)+"条")
            else:
                self.ui.label_QueryResuat.setText("尚无符合条件的文献")
        except Exception:
            print(Exception.__str__())

    #计算总页数
    def caculateTotoalPage(self):
        totoalPage = self.totalRecord//self.eachPageRecord
        if self.totalRecord % self.eachPageRecord > 0 :
            totoalPage += 1
        return totoalPage

    #刷新页面显示标志
    def updateLable(self):
        self.ui.label_CurrentPage.setText(str(self.currentPage+1))
        self.ui.label_TotalPages.setText(str(self.totalPages))

    #槽，执行重新载入
    def onRefresh(self):
        self.condition = ""
        self.ui.lineEdit_SearchContext.setText("")
        self.ui.comboBox_SearchWhat.setCurrentIndex(0)
        self.totalRecord = self.getTotalRecord()
        self.ui.label_TotalRecord.setText("共收录文档" + str(self.totalRecord) + "条")
        self.totalPages = self.caculateTotoalPage()
        self.currentPage = 0
        self.ui.label_QueryResuat.setText("")
        self.updateLable()
        self.executeQuery(0)
    #槽，设置每页显示记录数
    def oneachPageRecord(self):
        index = self.ui.comboBox_EachPageRecord.currentIndex()
        if index == 0:
            self.eachPageRecord = 20
        elif index == 1:
            self.eachPageRecord = 40
        elif index == 2:
            self.eachPageRecord = 60
        elif index == 3:
            self.eachPageRecord = 80
        elif index == 4:
            self.eachPageRecord = 100
        self.totalPages = self.caculateTotoalPage()
        self.ui.label_TotalPages.setText(str(self.totalPages))
        self.currentPage = 0
        self.executeQuery(0)
        self.updateLable()

    #槽，执行条件查询
    def onQuery(self):
        searchWhatIndex = self.ui.comboBox_SearchWhat.currentIndex()
        searchContext = self.ui.lineEdit_SearchContext.text().strip()
        if searchContext == "":
            QMessageBox.information(self,"提示!","请输入要查询的内容！",QMessageBox.Ok)
            return
        else:
            self.condition = self.getConditon(searchWhatIndex,searchContext)
            self.caculateConditionRecord()
            if self.totalRecord < 0:
                self.totalPages = 0
                self.currentPage = -1
                self.updateLable()
                self.executeQuery(0)
            else:
                self.totalPages = self.caculateTotoalPage()
                self.currentPage = 0
                self.updateLable()
                self.executeQuery(0)
    #获取条件查询的条件内容
    def getConditon(self,index,context):
        if index == 0:
            return "TITLE LIKE \'%%%s%%\'" % context
        elif index == 1:
            return "AUTHOR LIKE \'%%%s%%\'" % context
        elif index == 2:
            return "KEYWORDS LIKE \'%%%s%%\'" % context
        elif index == 3:
            return "ABSTRACT LIKE \'%%%s%%\'" % context
    #翻页下的执行查询
    def executeQuery(self,index):
        try:
            if self.condition == "":
                query = "SELECT TITLE,AUTHOR,SOURCE,YEAR,KEYWORDS,ABSTRACT,FL1ST,FL2ND,PAGES,ATPAGE,VOLUMN,PERIODS,AUTHORUNIT,SERIES,VENUE,TEACHER,MD5,ID FROM INFO LIMIT %d,%d" % (index,self.eachPageRecord)
            else:
                query = "SELECT TITLE,AUTHOR,SOURCE,YEAR,KEYWORDS,ABSTRACT,FL1ST,FL2ND,PAGES,ATPAGE,VOLUMN,PERIODS,AUTHORUNIT,SERIES,VENUE,TEACHER,MD5,ID FROM INFO WHERE %s LIMIT %d,%d" % (self.condition,index,self.eachPageRecord)
            self.queryModel.setQuery(query)
            self.mapper.toFirst()
        except Exception:
            print(Exception.__str__())

    #上一页
    def onPageUp(self):
        if self.currentPage - 1 >= 0 :
            self.currentPage -= 1
            self.executeQuery(self.currentPage * self.eachPageRecord)
            self.ui.label_CurrentPage.setText(str(self.currentPage+1))
    #下一页
    def onPageDown(self):
        if self.currentPage + 1 < self.totalPages:
            self.currentPage += 1
            self.executeQuery(self.currentPage*self.eachPageRecord)
            self.ui.label_CurrentPage.setText(str(self.currentPage+1))

    #跳转页面
    def onGotoPage(self):
        try:
            if self.ui.lineEdit_TargetPage.text().isdigit() :
                pageNum = int(self.ui.lineEdit_TargetPage.text())
                if pageNum >0 and pageNum<=self.totalPages:
                    self.currentPage = pageNum -1
                    self.executeQuery(self.currentPage * self.eachPageRecord)
                    self.ui.label_CurrentPage.setText(str(self.currentPage + 1))
                else:
                    QMessageBox.warning(self, "警告", "请输入正确页码范围", QMessageBox.Ok)
            else:
                QMessageBox.warning(self,"警告","请输入数字页码",QMessageBox.Ok)
        except Exception:
            print(Exception.__str__())

    #添加数据
    def onInsertData(self):
        insertDetailWidge = InsertDetailWidget(self.sqlQuery)
        insertDetailWidge.exec_()
    #删除数据
    def onDelete(self):
        try:
            curRec = self.queryModel.record(self.ui.tableView.currentIndex().row())
            title = curRec.value("TITLE")
            idd = curRec.value('ID')
            md5 = curRec.value('MD5')
            result = QMessageBox.question(self,"删除提示","文献资料《" + title + "》及数据信息将删除,是否删除？",QMessageBox.Ok|QMessageBox.No)
            if (result == QMessageBox.Ok) :
                print(1024)
                self.sqlQuery.prepare("DELETE FROM INFO where ID = :id")
                self.sqlQuery.bindValue(":id",idd)
                if(self.sqlQuery.exec() == False):
                    QMessageBox.critical(self,"错误","删除文献记录出现错误\n" + self.sqlQuery.lastError().text())
                else:
                    if md5 != "":
                        self.sqlQuery.prepare("DELETE FROM INFOFILE WHERE MD5 = :md5")
                        self.sqlQuery.bindValue(":md5",md5)
                        if (self.sqlQuery.exec()==False):
                            QMessageBox.critical(self, "错误", "删除文献PDF出现错误,请手动删除\n" + self.sqlQuery.lastError().text())
                    sqlStr = self.queryModel.query().executedQuery()
                    self.queryModel.setQuery(sqlStr)
            elif (result == QMessageBox.No):
                return
        except Exception:
            print(Exception.__str__())

    #修改数据
    def onUpdata(self):
        updateDetailWidget = UpdateDetailWidget(self.sqlQuery,self.queryModel.record(self.mapper.currentIndex()))
        updateDetailWidget.exec_()

    def getFLIndex(self, f2):
        if f2 == 'TS':
            return 0
        if f2 == 'QK':
            return 1
        if f2 == 'BZ':
            return 2
        if f2 == 'XL':
            return 3
        if f2 == 'HL':
            return 4
        if f2 == 'YB':
            return 5
        if f2 == 'WY':
            return 6

    def getDBIndex(self, f1):
        if f1 == 'DAWW':
            return 0
        if f1 == 'GDSL':
            return 1
        if f1 == 'YWWX':
            return 2
        if f1 == 'XDYW':
            return 3
        return -1
