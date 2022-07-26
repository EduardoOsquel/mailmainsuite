from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class settingsTunnel(QWidget):
    def __init__(self):
        super(settingsTunnel, self).__init__()
        loadUi("gui/settings.ui", self)
        
        self.pushClose.clicked.connect(self.pushClose_Control)
        
        #self.noAuth = False
        self.checkAuthBox.stateChanged.connect(self.frameAuth_Control)
    
    def frameAuth_Control(self):
        if not self.frameAuth.isEnabled():
            self.frameAuth.setEnabled(True)
        
    
    def pushClose_Control(self):
        self.close()