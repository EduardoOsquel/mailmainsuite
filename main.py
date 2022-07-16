from ast import Lambda
from fileinput import close
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, uic
import sys

from youtube_dl import main

class mainTunnel(QMainWindow):
    def __init__(self):
        super(mainTunnel, self).__init__()
        uic.loadUi("gui/interface.ui", self)
        
        #app = QApplication(sys.argv)
        
        #window = uic.loadUi("gui/interface.ui")
        #window.show()
        
        #window.actionExit.triggered.connect(self.actionExit)
        self.actionExit.triggered.connect(self.actionExit_Control)
        #app.exec()         
        
    def actionExit_Control(self):
        sys.exit()
        
#mainTunnel()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = mainTunnel()
    appWindow.show()
    
    sys.exit(app.exec_())