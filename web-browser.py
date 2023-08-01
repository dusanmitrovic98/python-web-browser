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
        screen = QDesktopWidget().screenGeometry()
        # x = 0
        # y = 0
        # self.progress_bar.move(x, y)

        self.progress_bar.setFixedHeight(4)
        self.progress_bar.setFixedWidth(screen.width())

        # Connect the webview's loadStarted signal to the show_progress_bar method
        self.webview.loadStarted.connect(self.show_progress_bar)

        # Connect the webview's loadProgress signal to the update_progress_bar method
        self.webview.loadProgress.connect(self.update_progress_bar)

        # Connect the webview's loadFinished signal to the hide_progress_bar method
        self.webview.loadFinished.connect(self.hide_progress_bar)

        # Connect the webview's urlChanged signal to the update_url method
        self.webview.urlChanged.connect(self.update_url)

        sidebar_layout = QHBoxLayout()
        # sidebar_layout.addWidget(self.sidebar)

        # Create a horizontal layout for the address bar and buttons
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.address_bar)

        # Create the minimize, maximize, and close buttons
        self.minimize_button = QPushButton(MINIMIZE_BUTTON, self)
        self.minimize_button.setStyleSheet("""
                QPushButton {
                    height: 13px;
                    width: 13px;
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
        self.minimize_button.clicked.connect(self.showMinimized)
        self.restore_button = QPushButton(RESTORE_NORMAL_BUTTON, self)
        self.restore_button.setStyleSheet("""
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
                QPushButton:pressed {
                    background-color: #004499;
                }
            """)
        self.restore_button.clicked.connect(self.showNormal)
        self.maximize_button = QPushButton(MAXIMIZE_BUTTON, self)
        self.maximize_button.setStyleSheet("""
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
        self.maximize_button.clicked.connect(self.showMaximized)
        # self.maximize_button.clicked.connect(self.toggleFullscreen)
        self.close_button = QPushButton(CLOSE_BUTTON, self)
        self.close_button.setStyleSheet("""
                QPushButton {
                    height: 13px;
                    width: 13px;
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
        self.close_button.clicked.connect(self.close)

        nav_layout.addWidget(self.minimize_button)
        nav_layout.addWidget(self.restore_button)
        nav_layout.addWidget(self.maximize_button)
        nav_layout.addWidget(self.close_button)

        # Create a vertical layout for the webview and address bar
        layout = QVBoxLayout()
        layout.addLayout(sidebar_layout)
        layout.addLayout(nav_layout)
        layout.addWidget(self.webview)

        # Set the layout for the main window
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Load the default URL
        self.webview.setUrl(QUrl('https://www.google.com'))

    def show_progress_bar(self):
        self.progress_bar.show()

            """)
        self.restore_button.clicked.connect(self.showNormal)
        self.maximize_button = QPushButton(MAXIMIZE_BUTTON, self)
        self.maximize_button.setStyleSheet("""
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
        self.maximize_button.clicked.connect(self.showMaximized)
        # self.maximize_button.clicked.connect(self.toggleFullscreen)
        self.close_button = QPushButton(CLOSE_BUTTON, self)
        self.close_button.setStyleSheet("""
                QPushButton {
                    height: 13px;
                    width: 13px;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 16px;
                }

                QPushButton:hover {
                    background-color: #505254;
