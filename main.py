import schedule
import time

from config import *
from breaks import *


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

    schedule.every(SHORT_BREAK).minutes.do(mainWindow)
    schedule.every(LONG_BREAK).minutes.do(fullWindow)

    while True:
        schedule.run_pending()
        time.sleep(0.1)
