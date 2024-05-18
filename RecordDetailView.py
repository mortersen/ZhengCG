import os
from PyQt5.QtWidgets import QWidget,QFileDialog,QMessageBox
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import pyqtSignal

from threading import Thread

from UI.UI_RecordDetailView import Ui_RecordDetailView
import fitz


class RecordDetailView(QWidget):
    Signal_RecordDetailReadPDF = pyqtSignal(str,str)
    Signal_RecordDownloadPDF = pyqtSignal(str,str)
    signal_SaveOver = pyqtSignal(str)
    signal_Home = pyqtSignal()
    signal_Query = pyqtSignal()
    signal_goBackDB = pyqtSignal(str)

    def __init__(self,DB,MD5,ID=None):
        super().__init__()
        self.query = QSqlQuery(DB)
        self.MD5 = MD5
        self.id = ID
        self.title = ""

        self.signal_SaveOver.connect(self.on_saveOver)

        self.UI = Ui_RecordDetailView()
        self.UI.setupUi(self)

        self.UI.btn_pdfRead.released.connect(self.on_SendSignalReadPDF)
        self.UI.btn_pdfDownload.released.connect(self.on_SendSignalDownloadPDF)
        self.UI.btn_home.released.connect(self.on_SendHome)
        self.UI.btn_goback.released.connect(self.on_SendGoBackDB)
        self.UI.btn_search.released.connect(self.on_SendQuery)
        self.queryAndShow()

    def queryAndShow(self):
        try:
            if self.MD5!="":
                sqQuery = "select * from info where md5=?"
                self.query.prepare(sqQuery)
                self.query.bindValue(0,self.MD5)
            else:
                sqQuery = "select * from info where id=?"
                self.query.prepare(sqQuery)
                self.query.bindValue(0, self.id)
                self.UI.btn_pdfDownload.setDisabled(True)
                self.UI.btn_pdfRead.setDisabled(True)
            self.query.exec()
            self.query.last()
            self.UI.label_FL.setText(self.query.value("FL"))
            self.title = self.query.value("TITLE")
            self.first = self.query.value("FL1ST")
            self.UI.label_Title.setText(self.title)
            self.UI.label_Author.setText(self.query.value("AUTHOR"))
            self.UI.label_Year.setText(self.query.value("YEAR"))
            self.UI.label_Keywords.setText(self.query.value("KEYWORDS"))
            self.UI.label_Summary.setText(self.query.value("ABSTRACT"))
            self.UI.label_Source.setText(self.query.value("SOURCE"))
            self.UI.label_Series.setText(self.query.value("SERIES"))
            self.UI.label_Teacher.setText(self.query.value("TEACHER"))
            self.UI.label_AuthorUnit.setText(self.query.value("AUTHORUNIT"))
            self.UI.label_ATpage.setText(self.query.value("PAGES"))
            self.UI.label_Pages.setText(self.query.value("ATPAGE"))
            self.UI.label_Periods.setText(self.query.value("PERIODS"))
            self.UI.label_Volumn.setText(self.query.value("VOLUMN"))


        except Exception:
            print(Exception.__str__())
    #槽，阅读PDF
    def on_SendSignalReadPDF(self):
        self.Signal_RecordDetailReadPDF.emit(self.title,self.MD5)
    #槽，下载PDF
    def on_SendSignalDownloadPDF(self):
        newfileName,ok = QFileDialog.getSaveFileName(self, "文件下载到...", os.getcwd() + "\\" + self.title + ".pdf", "*.pdf")
        print(1)
        if ok:
            # self.docDoc.save(newfileName)
            def func():
                try:
                    sqQuery = "SELECT FILEBINARY from INFOFILE WHERE MD5=?"
                    self.query.prepare(sqQuery)
                    self.query.bindValue(0, self.MD5)
                    self.query.exec()
                    self.query.last()
                    fileStream = self.query.value("FILEBINARY")
                    pdf = fitz.open(None, bytes(fileStream), 'PDF')
                    pdf.save(newfileName)
                    self.signal_SaveOver.emit(newfileName)
                except Exception:
                    print(Exception.__str__())
            saveThread = Thread(target=func)
            saveThread.start()
        else:
            return
    #槽，提示下载成功
    def on_saveOver(self,name):
        QMessageBox.information(self, "提示", name + "文件下载成功！")
    #槽，发射回到主页面信息
    def on_SendHome(self):
        self.signal_Home.emit()

    #槽，发射后退到哪一个子库
    def on_SendGoBackDB(self):
        self.signal_goBackDB.emit(self.first)
    #槽，发射打开搜索页
    def on_SendQuery(self):
        self.signal_Query.emit()
