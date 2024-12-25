import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application's GUI """
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        pass

    def createActions(self):
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)
        # MacOS disables shortcuts by default (this may not be required for linux/windows machines)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())