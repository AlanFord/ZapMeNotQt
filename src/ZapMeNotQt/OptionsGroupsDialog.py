import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
import libraries


class OptionsGroupsDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(OptionsGroupsDialog, self).__init__()
        self.load_ui()
        if libraries.groups == 0:
            self.StandardButton.setChecked(True)
        elif libraries.groups == 1:
            self.ThirtyButton.setChecked(True)
        else:
            self.DiscreteButton.setChecked(True)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsGroupsDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        if self.StandardButton.isChecked():
            libraries.groups = 0
        elif self.ThirtyButton.isChecked():
            libraries.groups = 1
        else:
            libraries.groups = 2
