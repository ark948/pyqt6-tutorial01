import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QFont

# local imports

class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
        

    def initializeUI(self):
        """ Set up the application. """
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle("QMessageBox Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(100, 10)
        catalogue_label.setFont(QFont("Arial", 18))

        search_label = QLabel("Search the index for an author:", self)
        search_label.move(20, 40)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(240, 24)
        self.author_edit.setPlaceholderText("Enter names as: First Last")
        search_button = QPushButton("Search", self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors)

        search_button = QPushButton("Exit", self)
        search_button.move(50, 100)
        search_button.clicked.connect(self.exitProgram)
    
    # ? problem, html tags not displaying
    def searchAuthors(self):
        file = "files/authors.txt"
        try:
            with open(file, "r") as f:
                authors = [line.rstrip("\n") for line in f]
            if self.author_edit.text() in authors:
                QMessageBox.information(self, "Author Found", "Author found in catalogue!", QMessageBox.StandardButton.Ok)
            else:
                answer = QMessageBox.question(self,
                "Author Not Found", """<p>Author not found in catalogue.</p> <p>Do you wish to continue?</p>""",
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No)
                if answer == QMessageBox.StandardButton.No:
                    print("Closing application.")
                    self.close()
                if answer == QMessageBox.StandardButton.Yes:
                    pass
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error", f"""<p>File not found.</p> <p>Error {error}</p> Closing application.""", QMessageBox.StandardButton.Ok)
            self.close()

    # ? this is not the proper way
    def exitProgram(self):
        print("Program exit.")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())