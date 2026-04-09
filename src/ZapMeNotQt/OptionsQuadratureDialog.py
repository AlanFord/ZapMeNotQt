import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic

from GenericBodyDialog import GenericBodyDialog
import dataStructures
import libraries


class OptionsQuadratureDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/OptionsQuadratureDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def accept(self):
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

    def on_dialog_accepted(self):
        libraries.quadrature = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
