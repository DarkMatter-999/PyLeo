import schedule
import time
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QKeySequence, QShortcut

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("PyLeo")
        self.resize(400, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        shortcut = QShortcut(Qt.Key.Key_Escape, self)
        shortcut.activated.connect(self.close)

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.close()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":

    schedule.every(10).seconds.do(main)

    while True:
        schedule.run_pending()
        time.sleep(0.1)
