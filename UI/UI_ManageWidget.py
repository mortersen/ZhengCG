# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ManageWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageWidget(object):
    def setupUi(self, ManageWidget):
        ManageWidget.setObjectName("ManageWidget")
        ManageWidget.resize(905, 350)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(ManageWidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_SearchWhat = QtWidgets.QComboBox(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_SearchWhat.setFont(font)
        self.comboBox_SearchWhat.setObjectName("comboBox_SearchWhat")
        self.comboBox_SearchWhat.addItem("")
        self.comboBox_SearchWhat.addItem("")
        self.comboBox_SearchWhat.addItem("")
        self.comboBox_SearchWhat.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_SearchWhat)
        self.lineEdit_SearchContext = QtWidgets.QLineEdit(ManageWidget)
        self.lineEdit_SearchContext.setMinimumSize(QtCore.QSize(150, 24))
        self.lineEdit_SearchContext.setObjectName("lineEdit_SearchContext")
        self.horizontalLayout.addWidget(self.lineEdit_SearchContext)
        self.btn_Query = QtWidgets.QPushButton(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Query.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Query.setIcon(icon)
        self.btn_Query.setObjectName("btn_Query")
        self.horizontalLayout.addWidget(self.btn_Query)
        self.btn_Reload = QtWidgets.QPushButton(ManageWidget)
        self.btn_Reload.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PIC/Reflash.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Reload.setIcon(icon1)
        self.btn_Reload.setIconSize(QtCore.QSize(24, 24))
        self.btn_Reload.setAutoRepeat(False)
        self.btn_Reload.setFlat(True)
        self.btn_Reload.setObjectName("btn_Reload")
        self.horizontalLayout.addWidget(self.btn_Reload)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 20)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.label_QueryResuat = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_QueryResuat.setFont(font)
        self.label_QueryResuat.setText("")
        self.label_QueryResuat.setObjectName("label_QueryResuat")
        self.horizontalLayout_3.addWidget(self.label_QueryResuat)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_InsertData = QtWidgets.QPushButton(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_InsertData.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/PIC/addDocument.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_InsertData.setIcon(icon2)
        self.btn_InsertData.setObjectName("btn_InsertData")
        self.horizontalLayout_2.addWidget(self.btn_InsertData)
        self.btn_Delete = QtWidgets.QPushButton(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Delete.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/PIC/deleteDocument.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Delete.setIcon(icon3)
        self.btn_Delete.setObjectName("btn_Delete")
        self.horizontalLayout_2.addWidget(self.btn_Delete)
        self.btn_Update = QtWidgets.QPushButton(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Update.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/PIC/editDocument.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Update.setIcon(icon4)
        self.btn_Update.setObjectName("btn_Update")
        self.horizontalLayout_2.addWidget(self.btn_Update)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(0, 13)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableView = QtWidgets.QTableView(ManageWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_TotalRecord = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_TotalRecord.setFont(font)
        self.label_TotalRecord.setObjectName("label_TotalRecord")
        self.horizontalLayout_7.addWidget(self.label_TotalRecord)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox_EachPageRecord = QtWidgets.QComboBox(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_EachPageRecord.setFont(font)
        self.comboBox_EachPageRecord.setObjectName("comboBox_EachPageRecord")
        self.comboBox_EachPageRecord.addItem("")
        self.comboBox_EachPageRecord.addItem("")
        self.comboBox_EachPageRecord.addItem("")
        self.comboBox_EachPageRecord.addItem("")
        self.comboBox_EachPageRecord.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_EachPageRecord)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_PageUp = QtWidgets.QPushButton(ManageWidget)
        self.btn_PageUp.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/PIC/PageUp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_PageUp.setIcon(icon5)
        self.btn_PageUp.setIconSize(QtCore.QSize(24, 24))
        self.btn_PageUp.setFlat(True)
        self.btn_PageUp.setObjectName("btn_PageUp")
        self.horizontalLayout_5.addWidget(self.btn_PageUp)
        self.label_2 = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_CurrentPage = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CurrentPage.setFont(font)
        self.label_CurrentPage.setObjectName("label_CurrentPage")
        self.horizontalLayout_5.addWidget(self.label_CurrentPage)
        self.label_3 = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_TotalPages = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_TotalPages.setFont(font)
        self.label_TotalPages.setObjectName("label_TotalPages")
        self.horizontalLayout_5.addWidget(self.label_TotalPages)
        self.label_6 = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.btn_PageDown = QtWidgets.QPushButton(ManageWidget)
        self.btn_PageDown.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/PIC/PageDown.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_PageDown.setIcon(icon6)
        self.btn_PageDown.setIconSize(QtCore.QSize(24, 24))
        self.btn_PageDown.setFlat(True)
        self.btn_PageDown.setObjectName("btn_PageDown")
        self.horizontalLayout_5.addWidget(self.btn_PageDown)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_TargetPage = QtWidgets.QLineEdit(ManageWidget)
        self.lineEdit_TargetPage.setMinimumSize(QtCore.QSize(32, 0))
        self.lineEdit_TargetPage.setMaximumSize(QtCore.QSize(32, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_TargetPage.setFont(font)
        self.lineEdit_TargetPage.setText("")
        self.lineEdit_TargetPage.setObjectName("lineEdit_TargetPage")
        self.horizontalLayout_6.addWidget(self.lineEdit_TargetPage)
        self.label_7 = QtWidgets.QLabel(ManageWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.btn_Goto = QtWidgets.QPushButton(ManageWidget)
        self.btn_Goto.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_Goto.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/PIC/Goto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Goto.setIcon(icon7)
        self.btn_Goto.setIconSize(QtCore.QSize(24, 24))
        self.btn_Goto.setFlat(True)
        self.btn_Goto.setObjectName("btn_Goto")
        self.horizontalLayout_6.addWidget(self.btn_Goto)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 18)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.Layout_Detail = QtWidgets.QVBoxLayout()
        self.Layout_Detail.setObjectName("Layout_Detail")
        self.verticalLayout.addLayout(self.Layout_Detail)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 18)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.horizontalLayout_10.setStretch(0, 14)
        self.horizontalLayout_10.setStretch(1, 3)

        self.retranslateUi(ManageWidget)
        QtCore.QMetaObject.connectSlotsByName(ManageWidget)

    def retranslateUi(self, ManageWidget):
        _translate = QtCore.QCoreApplication.translate
        ManageWidget.setWindowTitle(_translate("ManageWidget", "Form"))
        self.comboBox_SearchWhat.setItemText(0, _translate("ManageWidget", "标题"))
        self.comboBox_SearchWhat.setItemText(1, _translate("ManageWidget", "作者"))
        self.comboBox_SearchWhat.setItemText(2, _translate("ManageWidget", "关键字"))
        self.comboBox_SearchWhat.setItemText(3, _translate("ManageWidget", "主要内容"))
        self.btn_Query.setText(_translate("ManageWidget", "查询"))
        self.btn_Reload.setToolTip(_translate("ManageWidget", "重新载入数据"))
        self.btn_InsertData.setText(_translate("ManageWidget", "添加"))
        self.btn_Delete.setText(_translate("ManageWidget", "删除"))
        self.btn_Update.setText(_translate("ManageWidget", "修改"))
        self.label_TotalRecord.setText(_translate("ManageWidget", "共收录文档11111条"))
        self.label.setText(_translate("ManageWidget", "每页"))
        self.comboBox_EachPageRecord.setItemText(0, _translate("ManageWidget", "20"))
        self.comboBox_EachPageRecord.setItemText(1, _translate("ManageWidget", "40"))
        self.comboBox_EachPageRecord.setItemText(2, _translate("ManageWidget", "60"))
        self.comboBox_EachPageRecord.setItemText(3, _translate("ManageWidget", "80"))
        self.comboBox_EachPageRecord.setItemText(4, _translate("ManageWidget", "100"))
        self.label_2.setText(_translate("ManageWidget", "第"))
        self.label_CurrentPage.setText(_translate("ManageWidget", "600"))
        self.label_3.setText(_translate("ManageWidget", "页"))
        self.label_4.setText(_translate("ManageWidget", "共"))
        self.label_TotalPages.setText(_translate("ManageWidget", "600"))
        self.label_6.setText(_translate("ManageWidget", "页"))
        self.label_5.setText(_translate("ManageWidget", "跳至"))
        self.label_7.setText(_translate("ManageWidget", "页"))
import RES.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageWidget = QtWidgets.QWidget()
    ui = Ui_ManageWidget()
    ui.setupUi(ManageWidget)
    ManageWidget.show()
    sys.exit(app.exec_())
