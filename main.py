import schedule
import time

from PyQt6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction

from config import *
from breaks import *
from tray import SystemTrayIcon
from settings import ConfigWindow 

class PyLeoApp:
    def __init__(self):
        self.event_exit_app = None
        """Called when the user clicks the Exit option from the system tray context menu"""

        self._app = QApplication([])
        self._app.setQuitOnLastWindowClosed(False)
        self._widget = QWidget()
        self._icon = SystemTrayIcon(QIcon("assets/leotrayicon.png"), self._widget)
        self._icon.event_exit_click = self.on_exit_click

        self._icon.event_start_break_click = self.on_start_break_click
        self._icon.event_start_long_break_click = self.on_start_long_break_click
        self._icon.event_start_settings = self.on_settings_click

        self._main_window = None
        self._full_window = None
        self._settings_window = None

        self._short_timer = QTimer(self._app)
        self._short_timer.timeout.connect(self.schedule_next_break)
        self._short_timer.start(Config.get("SHORT_BREAK") * 60 * 1000)

        self._long_timer = QTimer(self._app)
        self._long_timer.timeout.connect(self.schedule_next_long_break)
        self._long_timer.start(Config.get("LONG_BREAK") * 60 * 1000)


    def run(self):
        self._app.exec()

    def fire_exit_app(self):
        if self.event_exit_app:
            self.event_exit_app(self)

    def on_exit_click(self, sender):
        self.fire_exit_app() 

    def on_start_break_click(self, sender):
        if self._main_window is None:
            self._main_window = MainWindow()
        self._main_window.show()

    def on_start_long_break_click(self, sender):
        if self._full_window is None:
            self._full_window = FullWindow()
        self._full_window.show()

    def schedule_next_break(self):
        self.on_start_break_click(self)

    def schedule_next_long_break(self):
        self.on_start_long_break_click(self)

    def on_settings_click(self):
        if self._settings_window is None:
            self._settings_window = ConfigWindow()
        self._settings_window.show()

if __name__ == '__main__':
    config = Config()

    app = PyLeoApp()
    app.run()

