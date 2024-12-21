import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap, QFont

# Horizontal Box Layout
# IMPORTANT: layout managers cannot be parents for other widgets.
# only widgets can be parents for other widgets

class MainWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setMinimumWidth(500)
        self.setFixedHeight(60)
        self.setWindowTitle("QHBoxLayout Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        name_label = QLabel("New Username:")
        name_edit = QLineEdit()
        name_edit.setClearButtonEnabled(True)
        name_edit.textEdited.connect(self.checkUserInput)
        
        self.accept_button = QPushButton("Confirm")
        self.accept_button.setEnabled(False)
        self.accept_button.clicked.connect(self.close)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(name_label)
        main_h_box.addWidget(name_edit)
        main_h_box.addWidget(self.accept_button)
        self.setLayout(main_h_box)

    def checkUserInput(self, text):
        if len(text) > 0 and all(t.isalpha() or t.isdigit() for t in text):
            self.accept_button.setEnabled(True)
        else:
            self.accept_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())