import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QDialog, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap, QFont

# local imports

class NewUserDialog(QDialog):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.setModal(True) # user cannot interact with the rest as long as this dialog is resolved
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setFixedSize(360, 320)
        self.setWindowTitle("Register New User")
        self.setUpWindow()

    def setUpWindow(self):
        login_label = QLabel("Create New Account", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(90, 20)

        user_image = "images/new_user_icon.png"
        try:
            with open(user_image):
                user_label = QLabel(self)
                pixmap = QPixmap(user_image)
                user_label.setPixmap(pixmap)
                user_label.move(150, 60)
        except FileNotFoundError as error:
            print(f"Image was not found {error}")
        name_label = QLabel("Username:", self)
        name_label.move(20, 144)
        self.name_edit = QLineEdit(self)
        self.name_edit.resize(250, 24)
        self.name_edit.move(90, 140)
        full_name_label = QLabel("Full Name:", self)
        full_name_label.move(20, 174)
        full_name_edit = QLineEdit(self)
        full_name_edit.resize(250, 24)
        full_name_edit.move(90, 170)
        # Create password QLabel and QLineEdit widgets
        new_pswd_label = QLabel("Password:", self)
        new_pswd_label.move(20, 204)
        self.new_pswd_edit = QLineEdit(self)
        self.new_pswd_edit.setEchoMode(
        QLineEdit.EchoMode.Password)
        self.new_pswd_edit.resize(250, 24)
        self.new_pswd_edit.move(90, 200)
        confirm_label = QLabel("Confirm:", self)
        confirm_label.move(20, 234)
        self.confirm_edit = QLineEdit(self)
        self.confirm_edit.setEchoMode(
        QLineEdit.EchoMode.Password)
        self.confirm_edit.resize(250, 24)
        self.confirm_edit.move(90, 230)

        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.resize(320, 32)
        sign_up_button.move(20, 270)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        name_text = self.name_edit.text()
        pswd_text = self.new_pswd_edit.text()
        confirm_text = self.confirm_edit.text()
        if name_text == "" or pswd_text == "":
            QMessageBox.warning(self, "Error Message",
                "Please enter username or password values.",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        elif pswd_text != confirm_text:
            QMessageBox.warning(self, "Error Message", "The passwords you entered do not match.",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            with open("files/users.txt", 'a+') as f:
                f.write("\n" + name_text + " ")
                f.write(pswd_text)
            self.close()