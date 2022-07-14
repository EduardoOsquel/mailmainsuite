from PyQt5 import QtWidgets, uic
import sys

class start:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        window = uic.loadUi("gui/interface.ui")
        window.show()
        
        window.actionExit.triggered.connect(self.actionExit)
        app.exec()
    
    def actionExit(self):
        sys.exit()
        
start()