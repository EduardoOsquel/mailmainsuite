# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eduardo/Git/sshproxytunnel/gui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 152)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 152))
        MainWindow.setMaximumSize(QtCore.QSize(700, 152))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(700, 152))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/eduardo/Git/sshproxytunnel/gui/../icons/console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdit.setGeometry(QtCore.QRect(20, 30, 200, 28))
        self.userEdit.setObjectName("userEdit")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(20, 10, 58, 21))
        self.userLabel.setObjectName("userLabel")
        self.serverEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.serverEdit.setGeometry(QtCore.QRect(20, 80, 200, 28))
        self.serverEdit.setObjectName("serverEdit")
        self.serverLabel = QtWidgets.QLabel(self.centralwidget)
        self.serverLabel.setGeometry(QtCore.QRect(20, 60, 58, 21))
        self.serverLabel.setObjectName("serverLabel")
        self.pushLogin = QtWidgets.QPushButton(self.centralwidget)
        self.pushLogin.setGeometry(QtCore.QRect(590, 30, 90, 28))
        self.pushLogin.setObjectName("pushLogin")
        self.pushClose = QtWidgets.QPushButton(self.centralwidget)
        self.pushClose.setGeometry(QtCore.QRect(590, 80, 90, 28))
        self.pushClose.setObjectName("pushClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Server = QtWidgets.QAction(MainWindow)
        self.actionAdd_Server.setObjectName("actionAdd_Server")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionAdd_Server)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH Tunneling"))
        self.userLabel.setText(_translate("MainWindow", "User:"))
        self.serverLabel.setText(_translate("MainWindow", "Server:"))
        self.pushLogin.setText(_translate("MainWindow", "Login"))
        self.pushClose.setText(_translate("MainWindow", "Close"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAdd_Server.setText(_translate("MainWindow", "Add Server"))
        self.actionAdd_Server.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSettings.setText(_translate("MainWindow", "Proxy Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
