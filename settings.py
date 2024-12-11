from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QSpinBox, QDoubleSpinBox, QPushButton, QColorDialog, QLabel

from config import Config


class ConfigWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyLeo Configuration")
        self.setGeometry(100, 100, 400, 300)

        self.config = Config.config

        layout = QFormLayout()

        self.short_break_spinbox = QSpinBox(self)
        self.short_break_spinbox.setValue(self.config["SHORT_BREAK"])
        layout.addRow("Short Break (minutes):", self.short_break_spinbox)

        self.short_break_duration_spinbox = QDoubleSpinBox(self)
        self.short_break_duration_spinbox.setValue(self.config["SHORT_BREAK_DURATION"])
        self.short_break_duration_spinbox.setSingleStep(0.1)
        layout.addRow("Short Break Duration (minutes):", self.short_break_duration_spinbox)

        self.long_break_spinbox = QSpinBox(self)
        self.long_break_spinbox.setValue(self.config["LONG_BREAK"])
        layout.addRow("Long Break (minutes):", self.long_break_spinbox)

        self.long_break_duration_spinbox = QDoubleSpinBox(self)
        self.long_break_duration_spinbox.setValue(self.config["LONG_BREAK_DURATION"])
        self.long_break_duration_spinbox.setSingleStep(0.1)
        layout.addRow("Long Break Duration (minutes):", self.long_break_duration_spinbox)

        self.color_button = QPushButton("Choose Color", self)
        self.color_button.clicked.connect(self.choose_color)
        self.color_label = QLabel(f"Current Color: {self.config['COLOR']}", self)
        layout.addRow(self.color_button, self.color_label)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_config)
        layout.addRow(self.save_button)

        self.setLayout(layout)

    def choose_color(self):
        color = QColorDialog.getColor(QColor(self.config["COLOR"]), self, options=QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if color.isValid():
            self.config["COLOR"] = f"{color.red()},{color.green()},{color.blue()},{color.alpha()}"
            self.color_label.setText(f"Current Color: {self.config['COLOR']}")

    def save_config(self):
        self.config["SHORT_BREAK"] = self.short_break_spinbox.value()
        self.config["SHORT_BREAK_DURATION"] = self.short_break_duration_spinbox.value()
        self.config["LONG_BREAK"] = self.long_break_spinbox.value()
        self.config["LONG_BREAK_DURATION"] = self.long_break_duration_spinbox.value()

        print("Configuration saved:")
        print(self.config)

        Config.save()


