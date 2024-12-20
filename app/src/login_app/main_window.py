import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap, QFont

# local imports


class MainWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setMinimumSize(640, 426)
        self.setWindowTitle("Main Window")
        self.setUpMainWindow()

        # there is no show()
        # this window only appears after successful login

    def setUpMainWindow(self):
        hello = QLabel("Hey, you are here!!!", self)
        hello.move(50, 50)

    def closeEvent(self, event):
        # a QCloseEvent is sent
        answer = QMessageBox.question(self, "Quit Applicatino?", 
                                        "Are you sure you want to quit?", 
                                        QMessageBox.StandardButton.No |
                                        QMessageBox.StandardButton.Yes, 
                                        QMessageBox.StandardButton.Yes)
        if answer == QMessageBox.StandardButton.Yes:
            event.accept()
        elif answer == QMessageBox.StandardButton.No:
            event.ignore()