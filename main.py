import schedule
import time
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QKeySequence, QShortcut, QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("PyLeo")
        self.resize(400, 200)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # self.setWindowOpacity(0.8)
        self.setStyleSheet("QWidget {background-color: rgba(34,14,59,200);}")

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout(self.mainWidget)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.countdown = 10
        self.updateTimer()
        self.timer.start(1000)  # Update every second

        shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        shortcut.activated.connect(self.close)

    def updateTimer(self):
        self.label.setText(f"Time left: {self.countdown}")
        self.countdown -= 1
        if self.countdown < 0:
            self.timer.stop()
            self.close()

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.close()


class FullWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("PyLeo")
        self.showMaximized()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # self.setWindowOpacity(0.8)
        self.setStyleSheet("QWidget {background-color: rgba(34,14,59,100);}")

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout(self.mainWidget)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.skipButton.clicked.connect(self.close)
        self.layout.addWidget(self.skipButton)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)

        self.countdown = 10  # Initial countdown in seconds
        self.updateTimer()
        self.timer.start(1000)

        shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        shortcut.activated.connect(self.close)

    def updateTimer(self):
        time_left = QTime(0, 0, 0).addSecs(self.countdown)
        self.label.setText(f"Time left: {time_left.toString('hh:mm:ss')}")
        self.countdown -= 1
        if self.countdown < 0:
            self.timer.stop()
            self.close()

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.close()


def mainWindow():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

def fullWindow():
    app = QApplication([])
    window = FullWindow()
    window.show()
    app.exec()


if __name__ == "__main__":

    schedule.every(15).minutes.do(mainWindow)
    schedule.every(50).minutes.do(fullWindow)

    while True:
        schedule.run_pending()
        time.sleep(0.1)
