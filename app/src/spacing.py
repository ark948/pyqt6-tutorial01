import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Spacing Example")

        label = QLabel("Enter text")
        line_edit = QLineEdit()
        button = QPushButton("End")

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(label)
        main_v_box.addSpacing(30)
        main_v_box.addWidget(line_edit)
        main_v_box.addStretch()
        main_v_box.addWidget(button)
        main_v_box.setContentsMargins(40, 30, 40, 30)

        self.setLayout(main_v_box)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())