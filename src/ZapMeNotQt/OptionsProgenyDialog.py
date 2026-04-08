import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
import libraries


class OptionsProgenyDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(OptionsProgenyDialog, self).__init__()
        self.load_ui()
        self.checkBox.setChecked(libraries.progeny)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsProgenyDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        libraries.progeny = self.checkBox.isChecked()
