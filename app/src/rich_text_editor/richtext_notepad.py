import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QTextCursor, QColor, QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QMessageBox, QTextEdit, QFileDialog, QInputDialog,
    QFontDialog, QColorDialog
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application's GUI """
        self.setMinimumSize(400, 500)

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        """ Create and arrange widgets in the main window. """
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.removeHighlights)
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        """ Create the application's menu actions. """
        # File Menu
        self.new_act = QAction(QIcon("images/icons/new_file.png"), "New")
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.triggered.connect(self.clearText)

        self.open_act = QAction(QIcon("images/icons/open_file.png"), "Open")
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.triggered.connect(self.openFile)

        self.save_act = QAction(QIcon("images/icons/save_file.png"), "Save")
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.triggered.connect(self.saveToFile)

        self.quit_act = QAction(QIcon("images/icons/exit.png"), "Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        # Edit Menu
        self.undo_act = QAction(QIcon("images/icons/undo.png"), "Undo")
        self.undo_act.setShortcut("Ctrl+Z")
        self.undo_act.triggered.connect(self.text_edit.undo)

        self.redo_act = QAction(QIcon("images/icons/redo.png"), "Redo")
        self.redo_act.setShortcut("Ctrl+Shift+Z")
        self.redo_act.triggered.connect(self.text_edit.redo)

        self.cut_act = QAction(QIcon("images/icons/cut.png"), "Cut")
        self.cut_act.setShortcut("Ctrl+X")
        self.cut_act.triggered.connect(self.text_edit.cut)

        self.copy_act = QAction(QIcon("images/icons/copy.png"), "Copy")
        self.copy_act.setShortcut("Ctrl+C")
        self.copy_act.triggered.connect(self.text_edit.copy)

        self.paste_act = QAction(QIcon("images/icons/paste.png"), "Paste")
        self.paste_act.setShortcut("Ctrl+V")
        self.paste_act.triggered.connect(self.text_edit.paste)

        self.find_act = QAction(QIcon("images/icons/find.png"), "Find All")
        self.find_act.setShortcut("Ctrl+F")
        self.find_act.triggered.connect(self.searchText)

        # Create actions for Tools menu
        self.font_act = QAction(QIcon("images/icons/font.png"), "Font")
        self.font_act.setShortcut("Ctrl+T")
        self.font_act.triggered.connect(self.chooseFont)

        self.color_act = QAction(QIcon("images/icons/color.png"), "Color")
        self.color_act.setShortcut("Ctrl+Shift+C")
        self.color_act.triggered.connect(self.chooseFontColor)

        self.highlight_act = QAction(QIcon("images/icons/highlight.png"), "Highlight")
        self.highlight_act.setShortcut("Ctrl+Shift+H")
        self.highlight_act.triggered.connect(self.chooseFontBackgroundColor)

        # Create actions for help menu
        self.about_act = QAction("About")
        self.about_act.triggered.connect(self.aboutDialog)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)
        # MacOS disables shortcuts by default (this may not be required for linux/windows machines)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)
        file_menu.addSeparator()
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        # Create Edit menu and add actions
        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.undo_act)
        edit_menu.addAction(self.redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.cut_act)
        edit_menu.addAction(self.copy_act)
        edit_menu.addAction(self.paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.find_act)

        # Create Tools menu and add actions
        tool_menu = self.menuBar().addMenu("Tools")

        tool_menu.addAction(self.font_act)
        tool_menu.addAction(self.color_act)
        tool_menu.addAction(self.highlight_act)
        
        # Create Help menu and add actions
        help_menu = self.menuBar().addMenu("Help")
        help_menu.addAction(self.about_act)

    def clearText(self):
        """ Clear the QTextEdit field. """
        answer = QMessageBox.question(
            self,
            "Clear Text",
            "Do you want to clear the text?",
            QMessageBox.StandardButton.No |
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.Yes
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.text_edit.clear()

    def openFile(self):
        """ Open a text or html file and display its contents. """
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "HTML Files (*.html);;Text Files (*.txt)"
        )
        if file_name:
            with open(file_name, "r") as f:
                notepad_text = f.read()
            self.text_edit.setText(notepad_text)

    def saveToFile(self):
        """If the save button is clicked, display dialog asking user if they want to save the text to a text or rich text file."""
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "HTML Files (*.html);;Text Files (*.txt)"
        )

        if file_name.endswith(".txt"):
            notepad_text = self.text_edit.toPlainText()
            with open(file_name, 'w') as f:
                f.write(notepad_text)
        elif file_name.endswith(".html"):
            notepad_text = self.text_edit.toHtml()
            with open(file_name, "w") as f:
                f.write(notepad_text)
        else:
            QMessageBox.information(self, "Not Saved", "Text not saved.", QMessageBox.StandardButton.Ok)

    def searchText(self):
        """ Search for text. """
        find_text, ok = QInputDialog.getText(self, "Search Text", "Find:")
        if ok:
            extra_selections = []
            # Set the cursor to the beginning
            self.text_edit.moveCursor(
                QTextCursor.MoveOperation.Start
            )
            color = QColor(Qt.GlobalColor.gray)
            while(self.text_edit.find(find_text)):
                # Use ExtraSelection() to mark the text you are searching for as gray
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                # Set the cursor of the selection
                selection.cursor = self.text_edit.textCursor()
                extra_selections.append(selection)
            # Highlight all selections in the QTextEdit widget
            self.text_edit.setExtraSelections(
                extra_selections
            )

    def removeHighlights(self):
        """ Reset extra selections after editing text. """
        self.text_edit.setExtraSelections([])

    def chooseFont(self):
        """Select a font from the QFontDialog."""
        current = self.text_edit.currentFont()
        opt = QFontDialog.FontDialogOption.DontUseNativeDialog
        font, ok = QFontDialog.getFont(current, self, options=opt)
        if ok:
            self.text_edit.setCurrentFont(font)

            

    def chooseFontColor(self):
        """Select a font from the QColorDialog."""
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)


    def chooseFontBackgroundColor(self):
        """Select a color for text's background."""
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextBackgroundColor(color)


    def aboutDialog(self):
        """Display the About dialog."""
        QMessageBox.about(self, "About Notepad", """<p>Beginner's Practical Guide to PyQt</p><p>Project 5.1 - Notepad GUI</p>""")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())