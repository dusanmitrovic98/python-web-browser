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
