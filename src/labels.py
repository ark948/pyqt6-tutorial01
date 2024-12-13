import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont

# local imports
from labels import setUpMainWindow

class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Basic Window")
        self.setUpMainWindow()
        self.show()

    
    def setUpMainWindow(self):
        """ Create QLabel to be displayed in the main window. """
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105, 15)
        
        image = "images/world.png"

        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print("Image was not found")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
