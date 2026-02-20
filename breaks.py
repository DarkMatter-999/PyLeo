from config import *
import random
from exercises import exercises
from PyQt6.QtCore import Qt, QTimer, QTime, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QKeySequence, QShortcut, QFont, QPixmap

class MainWindow(QMainWindow):
    break_finished = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("PyLeo")
        self.resize(400, 200)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget {background-color: rgba(" + Config.get("COLOR") +");}")

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout(self.mainWidget)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.toplabel = QLabel(self)
        self.toplabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toplabel.setWordWrap(True)
        self.toplabel.setGeometry(0, 0, 400, 200)
        font = self.toplabel.font()
        font.setPointSize(14)
        self.toplabel.setFont(font)
        self.layout.addWidget(self.toplabel)

        self.toplabel.setText(random.choice(exercises)[0])

        self.imageLabel = QLabel(self)
        pixmap = QPixmap("./assets/pyleo2.png")
        resized_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.imageLabel.setPixmap(resized_pixmap)
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.imageLabel)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(0, 0, 400, 200)
        font = self.label.font()
        font.setPointSize(24)
        self.label.setFont(font)
        self.layout.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)

        self.countdown = Config.get("SHORT_BREAK_DURATION") * 60
        self.updateTimer()
        self.timer.start(1000)  # Update every second

        shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        shortcut.activated.connect(self.close_window)

    def updateTimer(self):
        time_left = QTime(0, 0, 0).addSecs(int(self.countdown))
        self.label.setText(f"Time left: {time_left.toString('mm:ss')}")
        self.countdown -= 1
        if self.countdown < 0:
            self.timer.stop()
            self.close_window()

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.close_window()

    def close_window(self):
        self.break_finished.emit()
        self.deleteLater()

class FullWindow(QMainWindow):
    break_finished = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("PyLeo")
        self.showMaximized()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget {background-color: rgba(" + Config.get("COLOR") +");}")

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout(self.mainWidget)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.toplabel = QLabel(self)
        self.toplabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toplabel.setWordWrap(True)
        self.toplabel.setGeometry(0, 0, 600, 200)
        font = self.toplabel.font()
        font.setPointSize(14)
        self.toplabel.setFont(font)
        self.layout.addWidget(self.toplabel)

        self.toplabel.setText(random.choice(exercises)[0])

        self.imageLabel = QLabel(self)
        pixmap = QPixmap("./assets/pyleo1.png")
        resized_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.imageLabel.setPixmap(resized_pixmap)
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.imageLabel)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.label.font()
        font.setPointSize(24)
        self.label.setFont(font)
        self.layout.addWidget(self.label)

        self.skipButton = QPushButton("Skip Timer", self)
        self.skipButton.setFont(QFont("Any", 24))
        self.skipButton.clicked.connect(self.close_window)
        self.layout.addWidget(self.skipButton)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)

        self.countdown = Config.get("LONG_BREAK_DURATION") * 60
        self.updateTimer()
        self.timer.start(1000)

        shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        shortcut.activated.connect(self.close_window)

    def updateTimer(self):
        time_left = QTime(0, 0, 0).addSecs(int(self.countdown))
        self.label.setText(f"Time left: {time_left.toString('hh:mm:ss')}")
        self.countdown -= 1
        if self.countdown < 0:
            self.timer.stop()
            self.close_window()

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.close_window()

    def close_window(self):
        self.break_finished.emit()
        self.deleteLater()



