import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setMinimumSize(400, 160)
        self.setWindowTitle("Base")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())