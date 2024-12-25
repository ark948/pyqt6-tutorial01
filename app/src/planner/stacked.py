import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QStackedLayout, QFormLayout, QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setFixedSize(300, 340)
        self.setWindowTitle("QStackedLayout Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """ Create and arrange widgets in the main window """
        # Create and connect the combo box to switch pages
        page_combo = QComboBox()
        page_combo.addItems(["Image", "Description", "Additional Info"])
        page_combo.activated.connect(self.switchPage)

        # Create the Image page (page 1)
        profile_image = QLabel()
        pixmap = QPixmap("images/cat.jpg")
        profile_image.setPixmap(pixmap)
        profile_image.setScaledContents(True) # tells label to use all available space to display the content

        # Create the Profile page (Page 2)
        pg2_form = QFormLayout()
        pg2_form.setFieldGrowthPolicy(pg2_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg2_form.setFormAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        pg2_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg2_form.addRow("Breed: ", QLabel("Norwegian Forest Cat"))
        pg2_form.addRow("Origin: ", QLabel("Norway"))
        pg2_form.addRow(QLabel("Description:"))
        default_text = """Have a long, sturdy body, long legs and a bushy tail. They are friendly, intelligent, and generally good with people."""
        pg2_form.addRow(QTextEdit(default_text))

        pg2_container = QWidget()
        pg2_container.setLayout(pg2_form)

        # a layout cannot be added to QStackedLayout, instead, a container widget is created to group these widgets together.
        # QWidget can serve as a basic container for other widgets.

        # Create the About page (Page 3)
        pg3_form = QFormLayout()
        pg3_form.setFieldGrowthPolicy(pg3_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg3_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        pg3_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg3_form.addRow(QLabel("Enter your cat's info."))
        pg3_form.addRow("Name:", QLineEdit())
        pg3_form.addRow("Color:", QLineEdit())
        age_sb = QSpinBox()
        age_sb.setRange(0, 30)
        pg3_form.addRow("Age:", age_sb)
        weight_dsb = QDoubleSpinBox()
        weight_dsb.setRange(0.0, 30.0)
        pg3_form.addRow("Weight (kg):", weight_dsb)

        pg3_container = QWidget()
        pg3_container.setLayout(pg3_form)

        # Finally after creating the pages we'll create the Stacked Layout and add pages
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(profile_image)
        self.stacked_layout.addWidget(pg2_container)
        self.stacked_layout.addWidget(pg3_container)

        # Create the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(page_combo)
        main_v_box.addLayout(self.stacked_layout)

        # set the layout for main window
        self.setLayout(main_v_box)

    def switchPage(self, index):
        """ Slot for switching between tabs. """
        self.stacked_layout.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())