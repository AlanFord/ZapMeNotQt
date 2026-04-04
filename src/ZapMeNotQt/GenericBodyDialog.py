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
        self.name_field.currentIndexChanged.connect(self.on_name_selected)
        self.name_field.addItems(shield_dict.keys())
        # set the shell features to not visible as most dialogs won't use these
        self.shellCheckBox.setVisible(False)
        self.shellButton.setVisible(False)
        # TODO:  move this to a subclass
        # self.ShellDialog = ShellDialog()

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/GenericShieldDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_material_selected(self):
        self.density.setText(str(materials[self.material.currentText()]))

    def on_name_selected(self):
        new_name = self.name_field.currentText()
        if new_name in shield_dict:
            existing_shield = shield_dict[new_name]
            # loading the existing shield data into the dialog
            index = self.material.findText(existing_shield.material)
            if index != -1:
                self.material.setCurrentIndex(index)
            self.density.setText(existing_shield.density)
            self.radius1.setText(existing_shield.radius1)
            self.radius2.setText(existing_shield.radius2)
            self.triplet1X.setText(existing_shield.vector1[0])
            self.triplet1Y.setText(existing_shield.vector1[1])
            self.triplet1Z.setText(existing_shield.vector1[2])
            self.triplet2X.setText(existing_shield.vector2[0])
            self.triplet2Y.setText(existing_shield.vector2[1])
            self.triplet2Z.setText(existing_shield.vector2[2])
