import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path

from libraries import materials, shield_dict


class GenericBodyDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.material.addItems(materials.keys())
        self.material.setCurrentIndex(0)
        self.density.setText(str(materials[self.material.currentText()]))
        self.physical_validator = QDoubleValidator(0, 1e8, 5, self)
        self.density.setValidator(self.physical_validator)
        self.material.currentIndexChanged.connect(self.on_material_selected)
        self.name_field.addItems(shield_dict.keys())

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/GenericShieldDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_material_selected(self, index):
        self.density.setText(str(materials[self.material.currentText()]))
