import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path


class OptionsGroupsDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(OptionsGroupsDialog, self).__init__()
        self.load_ui()

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsGroupsDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
