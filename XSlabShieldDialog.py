import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path

from libraries import materials


class XSlabShieldDialog(PyQt6.QtWidgets.QDialog):
    def __init__(self):
        super(XSlabShieldDialog, self).__init__()
        self.load_ui()
        self.setWindowTitle("Semi-infinite X Slab Shield")
        self.material.addItems(materials.keys())
        self.material.setCurrentIndex(0)
        self.density.setText(str(materials[self.material.currentText()]))
        self.physical_validator = QDoubleValidator(0, 1e8, 5, self)
        self.density.setValidator(self.physical_validator)

        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("X-start (cm):")
        self.radius2Label.setText("X-end (cm):")
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

        self.material.currentIndexChanged.connect(self.on_material_selected)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/GenericShieldDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_material_selected(self, index):
        self.density.setText(str(materials[self.material.currentText()]))
