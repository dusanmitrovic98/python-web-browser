from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget, QDesktopWidget, QListWidget, QGridLayout, QProgressBar, QCompleter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import sys

BACKWARD_BUTTON = "<"
FORWARD_BUTTON = ">"
MINIMIZE_BUTTON = "-"
RESTORE_NORMAL_BUTTON = "⇓"
MAXIMIZE_BUTTON = "⇑"
CLOSE_BUTTON = "x"


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUI()
        self.setMouseTracking(True)
        self.drag_position = None

        # self.showMaximized()
        screen = QDesktopWidget().screenGeometry()

        # Calculate the center point of the screen
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center of the screen
        self.move(x, y)

    def initUI(self):
        self.setWindowTitle('QuickShark Browser')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #202124;
            }
        """)

        # Create the QWebEngineView
        self.webview = QWebEngineView(self)

        # Create the address bar
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)
        self.address_bar.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                font-size: 12px;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                height: 15px;
            }

            QLineEdit:focus {
            QPushButton:pressed {
                background-color: #004499;
            }
        """)
        self.forward_button.clicked.connect(self.webview.forward)

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
            border: none;
            background-color: grey;
            height: 5px;
            border-radius: 2.5px;
            }

            QProgressBar::chunk {
                background-color: red;
                width: 5px;
                margin: 0px;
            }
        """)
        self.progress_bar.hide()

        # Get the screen resolution
            QPushButton {
                height: 13px;
                width: 10px;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #505254;
            }

            QPushButton:pressed {
                background-color: #004499;
            }
        """)
        self.forward_button.clicked.connect(self.webview.forward)

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
