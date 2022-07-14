import sys
from PyQt5 import QtWidgets, uic

class start:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.window = uic.loadUi("gui/interface.ui")
        self.window.show()
        
        self.window.actionExit.triggered.connect(self.actionExit)
        app.exec()
    
    def actionExit(self):
        sys.exit()
        
start()