import os

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QFile, QIODeviceBase
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QDoubleValidator
from pathlib import Path
import libraries
import dataStructures
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


class DetectorDialog(QDialog):
    def __init__(self) -> None:
        super(DetectorDialog, self).__init__()
        self.load_ui()
        self.double_validator = QDoubleValidator(self)
        self.x_text.setValidator(self.double_validator)
        self.y_text.setValidator(self.double_validator)
        self.z_text.setValidator(self.double_validator)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self) -> None:
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/DetectorLocationDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        loader = QUiLoader()
        loader.load(ui_file, self)
        ui_file.close()

    def accept(self) -> None:
        # check the QTextFields for properly formatted
        #   numbers.  Call the dialog
        #   accept method only if all fields are valid.
        try:
            for field in [self.x_text, self.y_text, self.z_text]:
                # Get the text from the line edit
                text = field.text()
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

    def on_dialog_accepted(self) -> None:
        libraries.detector = dataStructures.Detector(self.x_text.text(),
                                                     self.y_text.text(),
                                                     self.z_text.text())
