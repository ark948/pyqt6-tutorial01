import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QPushButton example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.times_pressed = 0
        self.name_label = QLabel("Don't push the button.", self)
        self.name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        # this also can be set like this:
        # self.name_label.alignment = Qt.AlignmentFlag.AlignCenter

        self.name_label.move(60, 30)
        self.button = QPushButton("Push Me", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """ Handle when the button is clicked. """
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Why'd you press me?")
        if self.times_pressed == 2:
            self.name_label.setText("I'm warning you.")
            self.button.setText("Feelin Lucky")
            self.button.adjustSize()
            self.button.move(70, 70)
        if self.times_pressed == 3:
            print("The window has been closed.")
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())