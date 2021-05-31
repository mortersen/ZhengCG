# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/郑.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Search = QtWidgets.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PIC/书本查找.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Search.setIcon(icon1)
        self.action_Search.setObjectName("action_Search")
        self.action_YuWai = QtWidgets.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/PIC/域外文献.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_YuWai.setIcon(icon2)
        self.action_YuWai.setObjectName("action_YuWai")
        self.action_GuDaiShi = QtWidgets.QAction(mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/PIC/古代史料.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_GuDaiShi.setIcon(icon3)
        self.action_GuDaiShi.setObjectName("action_GuDaiShi")
        self.action_XianDai = QtWidgets.QAction(mainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/PIC/现代研究.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_XianDai.setIcon(icon4)
        self.action_XianDai.setObjectName("action_XianDai")
        self.action_DanAnWenWu = QtWidgets.QAction(mainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/PIC/档案与文物.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_DanAnWenWu.setIcon(icon5)
        self.action_DanAnWenWu.setObjectName("action_DanAnWenWu")
        self.action_Exit = QtWidgets.QAction(mainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/PIC/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon6)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Index = QtWidgets.QAction(mainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/PIC/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Index.setIcon(icon7)
        self.action_Index.setObjectName("action_Index")
        self.toolBar.addAction(self.action_Index)
        self.toolBar.addAction(self.action_Search)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_YuWai)
        self.toolBar.addAction(self.action_GuDaiShi)
        self.toolBar.addAction(self.action_XianDai)
        self.toolBar.addAction(self.action_DanAnWenWu)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Exit)

        self.retranslateUi(mainWindow)
        self.action_Exit.triggered.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "郑成功文献史料数据库"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.action_Search.setText(_translate("mainWindow", "检索页面"))
        self.action_YuWai.setText(_translate("mainWindow", "域外文献库"))
        self.action_GuDaiShi.setText(_translate("mainWindow", "古代史料库"))
        self.action_XianDai.setText(_translate("mainWindow", "现代研究文献库"))
        self.action_DanAnWenWu.setText(_translate("mainWindow", "档案与文物库"))
        self.action_Exit.setText(_translate("mainWindow", "退出"))
        self.action_Index.setText(_translate("mainWindow", "主页面"))
        self.action_Index.setToolTip(_translate("mainWindow", "主页面"))
import RES.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
