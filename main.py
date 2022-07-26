from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from readterminal import runCommand
import sys


class mainTunnel(QMainWindow):
    def __init__(self):
        super(mainTunnel, self).__init__()
        loadUi("gui/interface.ui", self)
        
        self.actionExit.triggered.connect(self.actionExit_Control)
        self.pushClose.clicked.connect(self.pushClose_Control)
        self.pushLogin.clicked.connect(self.pushLogin_Control)
        self.logged = logged = False
        
        
    def actionExit_Control(self):
        sys.exit()
        
    
    def actionSend_Control(self):
        runCommand()
        
    
    def pushClose_Control(self):
        sys.exit()
        
        
    def pushLogin_Control(self):
        logged = self.logged
        if not logged:
            self.pushLogin.setText("Logout")
            logged = True
        else:
            self.pushLogin.setText("Login")
            logged = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = mainTunnel()
    appWindow.show()
    
    sys.exit(app.exec_())