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
