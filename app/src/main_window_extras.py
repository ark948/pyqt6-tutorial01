import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
        QWidget, QCheckBox, QTextEdit, QDockWidget, QToolBar,
        QStatusBar, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Adding More Window Features")

        self.setUpMainWindow()
        self.createDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.setStatusBar(QStatusBar())

    def createActions(self):
        self.quit_act = QAction(
            QIcon("images/icons/exit.png"),
            "Quit"
        )
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Quit program")
        self.quit_act.triggered.connect(self.close)

        self.full_screen_act = QAction(
            "Full Screen", checkable=True
        )
        self.full_screen_act.setStatusTip("Switch to full screen mode")
        self.full_screen_act.triggered.connect(self.switchToFullScreen)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)
        
        view_menu = self.menuBar().addMenu("View")
        appearance_submenu = view_menu.addMenu("Appearance")
        appearance_submenu.addAction(self.full_screen_act)

    def switchToFullScreen(self, state):
        if state:
            self.showFullScreen()
        else:
            self.showNormal()

    def createToolBar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(self.quit_act)

    def createDockWidget(self):
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Formatting")
        dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.AllDockWidgetAreas
        )

        auto_bullet_cb = QCheckBox("Auto Bullet List")
        auto_bullet_cb.toggled.connect(self.changeTextEditSettings)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(auto_bullet_cb)
        dock_v_box.addStretch(1)

        dock_container = QWidget()
        dock_container.setLayout(dock_v_box)

        dock_widget.setWidget(dock_container)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

    def changeTextEditSettings(self, checked):
        if checked:
            self.text_edit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoBulletList
            )
        else:
            self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())