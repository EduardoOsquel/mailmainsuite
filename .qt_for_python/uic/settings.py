# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eduardo/Git/sshproxytunnel/gui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsForm(object):
    def setupUi(self, settingsForm):
        settingsForm.setObjectName("settingsForm")
        settingsForm.resize(410, 350)
        settingsForm.setMinimumSize(QtCore.QSize(410, 350))
        settingsForm.setMaximumSize(QtCore.QSize(410, 350))
        settingsForm.setBaseSize(QtCore.QSize(410, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/eduardo/Git/sshproxytunnel/gui/../icons/console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settingsForm.setWindowIcon(icon)
        self.proxyBox = QtWidgets.QGroupBox(settingsForm)
        self.proxyBox.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.proxyBox.setFlat(False)
        self.proxyBox.setObjectName("proxyBox")
        self.comboBox = QtWidgets.QComboBox(self.proxyBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 91, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.proxyEdit = QtWidgets.QLineEdit(self.proxyBox)
        self.proxyEdit.setGeometry(QtCore.QRect(10, 80, 271, 28))
        self.proxyEdit.setObjectName("proxyEdit")
        self.proxyLabel = QtWidgets.QLabel(self.proxyBox)
        self.proxyLabel.setGeometry(QtCore.QRect(10, 60, 58, 21))
        self.proxyLabel.setObjectName("proxyLabel")
        self.portEdit = QtWidgets.QLineEdit(self.proxyBox)
        self.portEdit.setGeometry(QtCore.QRect(290, 80, 91, 28))
        self.portEdit.setObjectName("portEdit")
        self.portLabel = QtWidgets.QLabel(self.proxyBox)
        self.portLabel.setGeometry(QtCore.QRect(290, 60, 58, 21))
        self.portLabel.setObjectName("portLabel")
        self.checkBox = QtWidgets.QCheckBox(self.proxyBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 130, 171, 21))
        self.checkBox.setObjectName("checkBox")
        self.frameAuth = QtWidgets.QFrame(self.proxyBox)
        self.frameAuth.setEnabled(False)
        self.frameAuth.setGeometry(QtCore.QRect(10, 160, 291, 121))
        self.frameAuth.setFrameShape(QtWidgets.QFrame.Box)
        self.frameAuth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameAuth.setObjectName("frameAuth")
        self.passwordEdit = QtWidgets.QLineEdit(self.frameAuth)
        self.passwordEdit.setEnabled(False)
        self.passwordEdit.setGeometry(QtCore.QRect(10, 80, 271, 28))
        self.passwordEdit.setObjectName("passwordEdit")
        self.userLabel = QtWidgets.QLabel(self.frameAuth)
        self.userLabel.setEnabled(False)
        self.userLabel.setGeometry(QtCore.QRect(10, 10, 58, 21))
        self.userLabel.setObjectName("userLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frameAuth)
        self.passwordLabel.setEnabled(False)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 60, 58, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.userEdit = QtWidgets.QLineEdit(self.frameAuth)
        self.userEdit.setEnabled(False)
        self.userEdit.setGeometry(QtCore.QRect(10, 30, 271, 28))
        self.userEdit.setObjectName("userEdit")
        self.frameAuth.raise_()
        self.comboBox.raise_()
        self.proxyEdit.raise_()
        self.proxyLabel.raise_()
        self.portEdit.raise_()
        self.portLabel.raise_()
        self.checkBox.raise_()
        self.pushClose = QtWidgets.QPushButton(settingsForm)
        self.pushClose.setGeometry(QtCore.QRect(300, 310, 90, 28))
        self.pushClose.setObjectName("pushClose")

        self.retranslateUi(settingsForm)
        QtCore.QMetaObject.connectSlotsByName(settingsForm)

    def retranslateUi(self, settingsForm):
        _translate = QtCore.QCoreApplication.translate
        settingsForm.setWindowTitle(_translate("settingsForm", "Settings"))
        self.proxyBox.setTitle(_translate("settingsForm", "Proxy Settings"))
        self.comboBox.setItemText(0, _translate("settingsForm", "HTTP"))
        self.comboBox.setItemText(1, _translate("settingsForm", "HTTPS"))
        self.proxyLabel.setText(_translate("settingsForm", "Proxy:"))
        self.portLabel.setText(_translate("settingsForm", "Port:"))
        self.checkBox.setText(_translate("settingsForm", "Proxy Authentication"))
        self.userLabel.setText(_translate("settingsForm", "User:"))
        self.passwordLabel.setText(_translate("settingsForm", "Password:"))
        self.pushClose.setText(_translate("settingsForm", "Close"))
