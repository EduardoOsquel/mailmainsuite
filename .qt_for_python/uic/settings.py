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
        settingsForm.resize(410, 340)
        settingsForm.setMinimumSize(QtCore.QSize(410, 340))
        settingsForm.setMaximumSize(QtCore.QSize(410, 340))
        settingsForm.setBaseSize(QtCore.QSize(410, 340))
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
        self.userLabel = QtWidgets.QLabel(self.proxyBox)
        self.userLabel.setEnabled(False)
        self.userLabel.setGeometry(QtCore.QRect(10, 160, 58, 21))
        self.userLabel.setObjectName("userLabel")
        self.userEdit = QtWidgets.QLineEdit(self.proxyBox)
        self.userEdit.setEnabled(False)
        self.userEdit.setGeometry(QtCore.QRect(10, 180, 271, 28))
        self.userEdit.setObjectName("userEdit")
        self.passwordLabel = QtWidgets.QLabel(self.proxyBox)
        self.passwordLabel.setEnabled(False)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 210, 58, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordEdit = QtWidgets.QLineEdit(self.proxyBox)
        self.passwordEdit.setEnabled(False)
        self.passwordEdit.setGeometry(QtCore.QRect(10, 230, 271, 28))
        self.passwordEdit.setObjectName("passwordEdit")
        self.pushClose = QtWidgets.QPushButton(settingsForm)
        self.pushClose.setGeometry(QtCore.QRect(300, 300, 90, 28))
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
