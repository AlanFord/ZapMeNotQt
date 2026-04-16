import os

from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path


class ScriptDisplayDialog(QDialog):
    def __init__(self, text_list):
        super().__init__()
        self.load_ui()
        display_text = ""
        for entry in text_list:
            display_text += entry + "\n"
        self.textEdit.setText(display_text)
        self.pushButton.clicked.connect(self.close)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/script_display.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
