from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from classes.settings import settingsTunnel
from classes.loadconf import LoadConf
from classes.saveconf import SaveConf
import sys


class mainTunnel(QMainWindow):
    def __init__(self):
        super(mainTunnel, self).__init__()
        loadUi("gui/interface.ui", self)
        
        
        self.logged = False
        
        self.actionExit.triggered.connect(self.actionExit_Control)
        self.actionSettings.triggered.connect(self.actionSettings_Control)
        self.pushClose.clicked.connect(self.pushClose_Control)
        self.pushLogin.clicked.connect(self.pushLogin_Control)
        
        self.popups = []
    
        
    def actionExit_Control(self):
        sys.exit()
        
        
    def actionSettings_Control(self):
        
        settingWin = settingsTunnel()
        settingWin.show()
        
        self.popups.append(settingWin)
        
        
    def actionSend_Control(self):
        runCommand()
        
    
    def pushClose_Control(self):
        sys.exit()
        
        
    def pushLogin_Control(self):
        if not self.logged:
            self.pushLogin.setText("Logout")
            self.logged = True
        else:
            self.pushLogin.setText("Login")
            self.logged = False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    appWindow = mainTunnel()
    appWindow.show()
    
    sys.exit(app.exec_())