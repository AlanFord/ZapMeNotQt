import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
import libraries


class RemoveShieldDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.comboBox.addItems(libraries.shield_dict.keys())
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/RemoveShieldDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        key = self.comboBox.currentText()
        del(libraries.shield_dict[key])
