import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path


class OptionsProgenyDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(OptionsProgenyDialog, self).__init__()
        self.load_ui()

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsProgenyDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
