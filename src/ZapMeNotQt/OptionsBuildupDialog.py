import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
import libraries


class OptionsBuildupDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.comboBox.addItems(libraries.buildup_factor_materials)
        if libraries.buildup_material != "None":
            index = self.comboBox.findText(libraries.buildup_material)
            if index != -1:
                self.comboBox.setCurrentIndex(index)
            else:
                self.comboBox.setCurrentIndex(0)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsBuildupDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        libraries.buildup_material = self.comboBox.currentText()
