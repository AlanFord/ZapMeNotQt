import os

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QFile, QIODeviceBase
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QDoubleValidator
from pathlib import Path

from ui.OptionsFillerDialog import Ui_Dialog

import libraries
''' '''
'''
ZapMeNotQt - a graphical user interface for ZapMeNot
Copyright (C) 2026  C. Alan Ford

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


class OptionsFillerDialog(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
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

    def on_material_selected(self) -> None:
        self.lineEdit.setText(str(libraries.materials[
            self.comboBox.currentText()]))

    def on_dialog_accepted(self) -> None:
        libraries.filler_material = self.comboBox.currentText()
        libraries.filler_density = self.lineEdit.text()

    def accept(self) -> None:
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
