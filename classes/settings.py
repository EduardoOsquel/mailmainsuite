from PyQt5.QtWidgets import QWidget, QFrame
from PyQt5.uic import loadUi


class settingsTunnel(QWidget):
    def __init__(self):
        super(settingsTunnel, self).__init__()
        loadUi("gui/settings.ui", self)
        
        self.pushClose.clicked.connect(self.pushClose_Control)
        
        #self.noAuth = False
        self.checkAuthBox.stateChanged.connect(self.frameAuth_Control)
        
    
    def frameAuth_Control(self):
        if self.checkAuthBox.isChecked():
            self.frameAuth.setEnabled(True)
            self.userEdit.setEnabled(True)
            self.userLabel.setEnabled(True)
            self.passwordEdit.setEnabled(True)
            self.passwordLabel.setEnabled(True)
        else:
            self.frameAuth.setEnabled(False)
            self.userEdit.setEnabled(False)
            self.userLabel.setEnabled(False)
            self.passwordEdit.setEnabled(False)
            self.passwordLabel.setEnabled(False)
    
    def pushClose_Control(self):
        self.close()