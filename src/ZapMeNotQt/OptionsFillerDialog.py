import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
import libraries


class OptionsFillerDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        # retain the option of no filler material in the model
        filler_list = ["None"]
        filler_list += libraries.materials.keys()
        self.comboBox.addItems(filler_list)
        index = self.comboBox.findText(libraries.filler_material)
        if index != -1:
            self.comboBox.setCurrentIndex(index)
        else:
            self.comboBox.setCurrentIndex(0)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/OptionsFillerDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        libraries.filler_material = self.comboBox.currentText()
