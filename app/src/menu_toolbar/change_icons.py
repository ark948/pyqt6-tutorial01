import sys, random
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application's GUI """
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Changing Icons Example")
        self.setWindowIcon(QIcon("images/icons/pyqt_logo.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        info_label = QLabel("Click on the button and select a fruit.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.images = [
            "images/icons/1_apple.png",
            "images/icons/2_pineapple.png",
            "images/icons/3_watermelon.png",
            "images/icons/4_banana.png"
        ]

        self.icon_button = QPushButton()
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addWidget(self.icon_button)
        
        container = QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def changeButtonIcon(self):
        self.icon_button.setIcon(
            QIcon(
                random.choice(self.images)
            )
        )
        self.icon_button.setIconSize(QSize(60, 60))


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())