import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path

from libraries import buildup_factor_materials


class OptionsBuildupDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(OptionsBuildupDialog, self).__init__()
        self.load_ui()

        self.comboBox.addItems(buildup_factor_materials)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsBuildupDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
