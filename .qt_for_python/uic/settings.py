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

        self.retranslateUi(settingsForm)
        QtCore.QMetaObject.connectSlotsByName(settingsForm)

    def retranslateUi(self, settingsForm):
        _translate = QtCore.QCoreApplication.translate
        settingsForm.setWindowTitle(_translate("settingsForm", "Settings"))
