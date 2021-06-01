# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SearchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchWidget(object):
    def setupUi(self, searchWidget):
        searchWidget.setObjectName("searchWidget")
        searchWidget.resize(560, 446)
        self.verticalLayout = QtWidgets.QVBoxLayout(searchWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(searchWidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comBox_WhatkindSearchFor = QtWidgets.QComboBox(self.widget_3)
        self.comBox_WhatkindSearchFor.setMinimumSize(QtCore.QSize(0, 28))
        self.comBox_WhatkindSearchFor.setObjectName("comBox_WhatkindSearchFor")
        self.comBox_WhatkindSearchFor.addItem("")
        self.comBox_WhatkindSearchFor.addItem("")
        self.comBox_WhatkindSearchFor.addItem("")
        self.comBox_WhatkindSearchFor.addItem("")
        self.comBox_WhatkindSearchFor.addItem("")
        self.comBox_WhatkindSearchFor.addItem("")
        self.comBox_WhatkindSearchFor.addItem("")
        self.horizontalLayout_2.addWidget(self.comBox_WhatkindSearchFor)
        self.lineEdit_WhatSearch = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_WhatSearch.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_WhatSearch.setStatusTip("")
        self.lineEdit_WhatSearch.setWhatsThis("")
        self.lineEdit_WhatSearch.setText("")
        self.lineEdit_WhatSearch.setObjectName("lineEdit_WhatSearch")
        self.horizontalLayout_2.addWidget(self.lineEdit_WhatSearch)
        self.btn_Search = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Search.sizePolicy().hasHeightForWidth())
        self.btn_Search.setSizePolicy(sizePolicy)
        self.btn_Search.setMinimumSize(QtCore.QSize(0, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Search.setIcon(icon)
        self.btn_Search.setObjectName("btn_Search")
        self.horizontalLayout_2.addWidget(self.btn_Search)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 8)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.groupBox = QtWidgets.QGroupBox(searchWidget)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_YUWAI = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_YUWAI.sizePolicy().hasHeightForWidth())
        self.checkBox_YUWAI.setSizePolicy(sizePolicy)
        self.checkBox_YUWAI.setMinimumSize(QtCore.QSize(0, 26))
        self.checkBox_YUWAI.setStyleSheet("background-color: rgb(100, 181, 246);\n"
"border-radius:5px;")
        self.checkBox_YUWAI.setChecked(True)
        self.checkBox_YUWAI.setTristate(False)
        self.checkBox_YUWAI.setObjectName("checkBox_YUWAI")
        self.horizontalLayout_4.addWidget(self.checkBox_YUWAI)
        self.checkBox_GUSHI = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_GUSHI.sizePolicy().hasHeightForWidth())
        self.checkBox_GUSHI.setSizePolicy(sizePolicy)
        self.checkBox_GUSHI.setMinimumSize(QtCore.QSize(0, 26))
        self.checkBox_GUSHI.setStyleSheet("background-color: rgb(100, 181, 246);\n"
"border-radius:5px;\n"
"")
        self.checkBox_GUSHI.setChecked(True)
        self.checkBox_GUSHI.setObjectName("checkBox_GUSHI")
        self.horizontalLayout_4.addWidget(self.checkBox_GUSHI)
        self.checkBox_XIANDAI = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_XIANDAI.sizePolicy().hasHeightForWidth())
        self.checkBox_XIANDAI.setSizePolicy(sizePolicy)
        self.checkBox_XIANDAI.setMinimumSize(QtCore.QSize(0, 26))
        self.checkBox_XIANDAI.setStyleSheet("background-color: rgb(100, 181, 246);\n"
"border-radius:5px;\n"
"")
        self.checkBox_XIANDAI.setChecked(True)
        self.checkBox_XIANDAI.setObjectName("checkBox_XIANDAI")
        self.horizontalLayout_4.addWidget(self.checkBox_XIANDAI)
        self.checkBox_DANGAN = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_DANGAN.sizePolicy().hasHeightForWidth())
        self.checkBox_DANGAN.setSizePolicy(sizePolicy)
        self.checkBox_DANGAN.setMinimumSize(QtCore.QSize(0, 26))
        self.checkBox_DANGAN.setStyleSheet("background-color: rgb(100, 181, 246);\n"
"border-radius:5px;\n"
"")
        self.checkBox_DANGAN.setChecked(True)
        self.checkBox_DANGAN.setAutoRepeat(False)
        self.checkBox_DANGAN.setObjectName("checkBox_DANGAN")
        self.horizontalLayout_4.addWidget(self.checkBox_DANGAN)
        self.horizontalLayout_5.addWidget(self.groupBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 12)
        self.horizontalLayout_5.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ResultWidget = QtWidgets.QWidget(searchWidget)
        self.ResultWidget.setObjectName("ResultWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ResultWidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.btn_allDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_allDB.sizePolicy().hasHeightForWidth())
        self.btn_allDB.setSizePolicy(sizePolicy)
        self.btn_allDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_allDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_allDB.setDefault(True)
        self.btn_allDB.setFlat(False)
        self.btn_allDB.setObjectName("btn_allDB")
        self.verticalLayout_5.addWidget(self.btn_allDB)
        self.btn_bookDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_bookDB.sizePolicy().hasHeightForWidth())
        self.btn_bookDB.setSizePolicy(sizePolicy)
        self.btn_bookDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_bookDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_bookDB.setDefault(True)
        self.btn_bookDB.setFlat(False)
        self.btn_bookDB.setObjectName("btn_bookDB")
        self.verticalLayout_5.addWidget(self.btn_bookDB)
        self.btn_newsPaparDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_newsPaparDB.sizePolicy().hasHeightForWidth())
        self.btn_newsPaparDB.setSizePolicy(sizePolicy)
        self.btn_newsPaparDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_newsPaparDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_newsPaparDB.setDefault(True)
        self.btn_newsPaparDB.setFlat(False)
        self.btn_newsPaparDB.setObjectName("btn_newsPaparDB")
        self.verticalLayout_5.addWidget(self.btn_newsPaparDB)
        self.btn_periodDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_periodDB.sizePolicy().hasHeightForWidth())
        self.btn_periodDB.setSizePolicy(sizePolicy)
        self.btn_periodDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_periodDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_periodDB.setDefault(True)
        self.btn_periodDB.setFlat(False)
        self.btn_periodDB.setObjectName("btn_periodDB")
        self.verticalLayout_5.addWidget(self.btn_periodDB)
        self.btn_ThesisDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ThesisDB.sizePolicy().hasHeightForWidth())
        self.btn_ThesisDB.setSizePolicy(sizePolicy)
        self.btn_ThesisDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_ThesisDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_ThesisDB.setDefault(True)
        self.btn_ThesisDB.setFlat(False)
        self.btn_ThesisDB.setObjectName("btn_ThesisDB")
        self.verticalLayout_5.addWidget(self.btn_ThesisDB)
        self.btn_conferencePaperDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conferencePaperDB.sizePolicy().hasHeightForWidth())
        self.btn_conferencePaperDB.setSizePolicy(sizePolicy)
        self.btn_conferencePaperDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_conferencePaperDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_conferencePaperDB.setDefault(True)
        self.btn_conferencePaperDB.setFlat(False)
        self.btn_conferencePaperDB.setObjectName("btn_conferencePaperDB")
        self.verticalLayout_5.addWidget(self.btn_conferencePaperDB)
        self.btn_reportDB = QtWidgets.QPushButton(self.ResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reportDB.sizePolicy().hasHeightForWidth())
        self.btn_reportDB.setSizePolicy(sizePolicy)
        self.btn_reportDB.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_reportDB.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#ffaa00;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ffd6be;\n"
"font:25 12pt \"微软雅黑 Light\";\n"
"}")
        self.btn_reportDB.setDefault(True)
        self.btn_reportDB.setFlat(False)
        self.btn_reportDB.setObjectName("btn_reportDB")
        self.verticalLayout_5.addWidget(self.btn_reportDB)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.verticalLayout_5.setStretch(6, 1)
        self.verticalLayout_5.setStretch(7, 1)
        self.verticalLayout_5.setStretch(8, 1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.TableViewLayout = QtWidgets.QVBoxLayout()
        self.TableViewLayout.setObjectName("TableViewLayout")
        self.horizontalLayout_7.addLayout(self.TableViewLayout)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)
        self.horizontalLayout_7.setStretch(2, 18)
        self.horizontalLayout_7.setStretch(3, 3)
        self.horizontalLayout.addWidget(self.ResultWidget)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.setStretch(0, 16)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 8)

        self.retranslateUi(searchWidget)
        self.comBox_WhatkindSearchFor.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(searchWidget)

    def retranslateUi(self, searchWidget):
        _translate = QtCore.QCoreApplication.translate
        searchWidget.setWindowTitle(_translate("searchWidget", "Form"))
        self.comBox_WhatkindSearchFor.setItemText(0, _translate("searchWidget", "图书"))
        self.comBox_WhatkindSearchFor.setItemText(1, _translate("searchWidget", "期刊"))
        self.comBox_WhatkindSearchFor.setItemText(2, _translate("searchWidget", "报纸"))
        self.comBox_WhatkindSearchFor.setItemText(3, _translate("searchWidget", "论文"))
        self.comBox_WhatkindSearchFor.setItemText(4, _translate("searchWidget", "会议论文"))
        self.comBox_WhatkindSearchFor.setItemText(5, _translate("searchWidget", "调研报告"))
        self.comBox_WhatkindSearchFor.setItemText(6, _translate("searchWidget", "全库文献"))
        self.lineEdit_WhatSearch.setToolTip(_translate("searchWidget", "输入查询内容"))
        self.lineEdit_WhatSearch.setPlaceholderText(_translate("searchWidget", "请输入您要搜索的关键字"))
        self.btn_Search.setText(_translate("searchWidget", "搜索"))
        self.groupBox.setTitle(_translate("searchWidget", "选择检索数据库"))
        self.checkBox_YUWAI.setText(_translate("searchWidget", "域外文献库"))
        self.checkBox_GUSHI.setText(_translate("searchWidget", "古代史料库"))
        self.checkBox_XIANDAI.setText(_translate("searchWidget", "现代研究文献库"))
        self.checkBox_DANGAN.setText(_translate("searchWidget", "档案与文物库"))
        self.btn_allDB.setText(_translate("searchWidget", "全库文献"))
        self.btn_bookDB.setText(_translate("searchWidget", "图 书"))
        self.btn_newsPaparDB.setText(_translate("searchWidget", "报 纸"))
        self.btn_periodDB.setText(_translate("searchWidget", "期 刊"))
        self.btn_ThesisDB.setText(_translate("searchWidget", "论 文"))
        self.btn_conferencePaperDB.setText(_translate("searchWidget", "会议论文"))
        self.btn_reportDB.setText(_translate("searchWidget", "调研报告"))
import RES.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchWidget = QtWidgets.QWidget()
    ui = Ui_searchWidget()
    ui.setupUi(searchWidget)
    searchWidget.show()
    sys.exit(app.exec_())
