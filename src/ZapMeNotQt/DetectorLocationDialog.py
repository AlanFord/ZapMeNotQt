import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path


class DetectorDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(DetectorDialog, self).__init__()
        self.load_ui()
        self.x_text.setValidator(QDoubleValidator())
        self.y_text.setValidator(QDoubleValidator())
        self.z_text.setValidator(QDoubleValidator())
        self.accepted.connect(self.log_new_values)
        self.x_value = "0.0"
        self.y_value = "0.0"
        self.z_value = "0.0"

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/DetectorLocationDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def log_new_values(self):
        self.x_value = self.x_text.text
        self.y_value = self.y_text.text
        self.z_value = self.z_text.text
