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
        settingsForm.resize(400, 300)
        settingsForm.setMinimumSize(QtCore.QSize(400, 300))
        settingsForm.setMaximumSize(QtCore.QSize(400, 300))
        settingsForm.setBaseSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/eduardo/Git/sshproxytunnel/gui/../icons/console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settingsForm.setWindowIcon(icon)
        self.pushClose = QtWidgets.QPushButton(settingsForm)
        self.pushClose.setGeometry(QtCore.QRect(290, 250, 90, 28))
        self.pushClose.setObjectName("pushClose")

        self.retranslateUi(settingsForm)
        QtCore.QMetaObject.connectSlotsByName(settingsForm)

    def retranslateUi(self, settingsForm):
        _translate = QtCore.QCoreApplication.translate
        settingsForm.setWindowTitle(_translate("settingsForm", "Settings"))
        self.pushClose.setText(_translate("settingsForm", "Close"))
