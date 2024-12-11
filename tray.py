from PyQt6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction

from breaks import *

class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super().__init__(icon, parent)
        self.event_play_click = None
        self.event_pause_click = None
        self.event_exit_click = None
        self.event_start_settings = None

        menu = QMenu(parent)

        self._start_break_action = QAction("Start Short break", parent)
        self._start_break_action.triggered.connect(self.on_start_break_click)
        menu.addAction(self._start_break_action)

        self._start_long_break_action = QAction("Start Long break", parent)
        self._start_long_break_action.triggered.connect(self.on_start_long_break_click)
        menu.addAction(self._start_long_break_action)

        self._settings_action = QAction("Settings", parent)
        self._settings_action.triggered.connect(self.on_settings_click)
        menu.addAction(self._settings_action)

        self._exit_action = QAction("Exit", parent)
        self._exit_action.triggered.connect(self.on_exit_click)
        menu.addAction(self._exit_action)

        self.setContextMenu(menu)

        # self.activated.connect(self.on_icon_click)
        self.show()

    def on_start_break_click(self):
        self.fire_start_break_click()

    def fire_start_break_click(self):
        if self.event_start_break_click:
            self.event_start_break_click(self)

    def on_start_long_break_click(self):
        self.fire_long_break_click()

    def fire_long_break_click(self):
        if self.event_start_long_break_click:
            self.event_start_long_break_click(self)

    def on_settings_click(self):
        self.fire_settings_click()

    def fire_settings_click(self):
        if self.event_start_settings:
            self.event_start_settings()

    def on_exit_click(self):
        self.fire_exit_click()
        print("Exiting")
        QApplication.quit()

    # def on_icon_click(self, reason):
    #     if reason == QSystemTrayIcon.ActivationReason.Trigger:
    #         new_icon = QIcon("assets/leotrayicon.png")
    #         self.setIcon(new_icon)
    
    def fire_exit_click(self):
        if self.event_exit_click:
            self.event_exit_click(self)

