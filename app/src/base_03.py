import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)


# QMainWindow vs QWidget:
# Everything in Qt inherits from QWidget
# a window is just a widget that is not placed within a parent
# QMainWindow focuses on creating and managing the layout for the main window of the application


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

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())