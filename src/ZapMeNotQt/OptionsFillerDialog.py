import os

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path
import libraries


class OptionsFillerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        # retain the option of no filler material in the model
        filler_list = ["None"]
        filler_list += libraries.materials.keys()
        self.comboBox.addItems(filler_list)
        index = self.comboBox.findText(libraries.filler_material)
        density = libraries.filler_density
        if index != -1:
            self.comboBox.setCurrentIndex(index)
            self.lineEdit.setText(density)
        else:
            self.comboBox.setCurrentIndex(0)
            self.lineEdit.setText("0.0")
        self.comboBox.currentIndexChanged.connect(self.on_material_selected)
        # create a validator for the density line edit widget
        self.positive_validator = QDoubleValidator(self)
        self.positive_validator.setBottom(0)
        self.lineEdit.setValidator(self.positive_validator)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/OptionsFillerDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_material_selected(self):
        self.lineEdit.setText(str(libraries.materials[
            self.comboBox.currentText()]))

    def on_dialog_accepted(self):
        libraries.filler_material = self.comboBox.currentText()
        libraries.filler_density = self.lineEdit.text()

    def accept(self):
        # check the QTextField for a properly formatted
        #   number.  Call the dialog
        #   accept method only if the field is valid.
        try:
            # Get the text from the line edit
            text = self.lineEdit.text()
            # Check if the value is valid
            float(text)
        except ValueError:
            # This handles cases where the text isn't a valid float
            if text == "":
                text = "A blank field"
            else:
                text = "The value " + text
            QMessageBox.critical(self, "Error",
                                 text + " is an invalid number format.")
        else:
            super().accept()
