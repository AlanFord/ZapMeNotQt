import os
from pathlib import Path

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QFile, QIODeviceBase
from PySide6.QtUiTools import QUiLoader

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


class OptionsQuadratureDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.load_ui()
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self) -> None:
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/OptionsQuadratureDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        loader = QUiLoader()
        loader.load(ui_file, self)
        ui_file.close()

    def accept(self) -> None:
        # first check the QTextFields for properly formatted
        #   numbers.  Then, if the shield name field is visible,
        #   check for a valid shield name.  Call the dialog
        #   accept method only if all fields are valid.
        try:
            for field in [self.triplet1X, self.triplet1Y, self.triplet1Z]:
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
                                 text + " is not an integer.")
        else:
            self.on_dialog_accepted()
            super().accept()

    def on_dialog_accepted(self) -> None:
        libraries.quadrature = [self.triplet1X.text(),
                                self.triplet1Y.text(),
                                self.triplet1Z.text()]
