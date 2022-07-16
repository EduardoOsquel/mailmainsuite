from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

class mainTunnel(QMainWindow):
    def __init__(self):
        super(mainTunnel, self).__init__()
        loadUi("gui/interface.ui", self)
        
        self.actionExit.triggered.connect(self.actionExit_Control)
        
    def actionExit_Control(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = mainTunnel()
    appWindow.show()
    
    sys.exit(app.exec_())