from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class settingsTunnel(QWidget):
    def __init__(self):
        super(settingsTunnel, self).__init__()
        loadUi("gui/settings.ui", self)
        
        self.pushClose.clicked.connect(self.pushClose_Control)
    
    
    def pushClose_Control(self):
        self.close()