import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt


# local imports
from registration import NewUserDialog
from main_window import MainWindow


class LoginWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setFixedSize(360, 220)
        self.setWindowTitle("Login GUI")

        self.setUpWindow()
        self.show()

    def setUpWindow(self):
        self.login_is_successful = False
        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)
        # Create widgets for username and password

        # username label and field
        username_label = QLabel("Username:", self)
        username_label.move(20, 54)
        self.username_edit = QLineEdit(self)
        self.username_edit.resize(250, 24)
        self.username_edit.move(90, 50)

        # password label and field
        password_label = QLabel("Password:", self)
        password_label.move(20, 86)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)

        # display password option
        self.show_password_cb = QCheckBox("Show Password", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(
            self.displayPasswordIfChecked
        )

        # Create QPushButton for signing in
        login_button = QPushButton("Login", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        # Create sign up QLabel and QPushButton
        not_member_label = QLabel("Not a member?", self)
        not_member_label.move(20, 186)

        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        users = {}
        file = "files/users.txt"
        try:
            with open(file, "r") as f:
                for line in f:
                    user_info = line.split(" ")
                    username_info = user_info[0]
                    password_info = user_info[1].strip("\n")
                    users[username_info] = password_info
            username = self.username_edit.text()
            password = self.password_edit.text()
            if (username, password) in users.items():
                QMessageBox.information(self, "Login Successful!", "Login Successful!",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.login_is_successful = True
                self.close()
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, "Error Message", "The username or password is incorrect.",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error", f"""<p>File not found.</p> <p>Error: {error}""", QMessageBox.StandardButton.Ok)
            # craete file if it does not exist, for signup
            f = open(file, "w")

    def displayPasswordIfChecked(self, checked):
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
    
    def createNewUser(self):
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()

    def openApplicationWindow(self):
        # open a mock window after user logs in
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        # a QCloseEvent is sent
        if self.login_is_successful == True:
            event.accept()
        else:
            answer = QMessageBox.question(self, "Quit Applicatino?", 
                                          "Are you sure you want to quit?", 
                                          QMessageBox.StandardButton.No |
                                          QMessageBox.StandardButton.Yes, 
                                          QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            elif answer == QMessageBox.StandardButton.No:
                event.ignore()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())