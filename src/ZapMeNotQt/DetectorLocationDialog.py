import os

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from PyQt6.QtGui import QDoubleValidator
from pathlib import Path
import libraries
import dataStructures


class DetectorDialog(QDialog):
    def __init__(self):
        super(DetectorDialog, self).__init__()
        self.load_ui()
        self.double_validator = QDoubleValidator(self)
        self.x_text.setValidator(self.double_validator)
        self.y_text.setValidator(self.double_validator)
        self.z_text.setValidator(self.double_validator)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/DetectorLocationDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def accept(self):
        # check the QTextFields for properly formatted
        #   numbers.  Call the dialog
        #   accept method only if all fields are valid.
        try:
            for field in [self.x_text, self.x_text, self.x_text]:
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

    def on_dialog_accepted(self):
        libraries.detector = dataStructures.Detector(self.x_text.text(),
                                                     self.y_text.text(),
                                                     self.z_text.text())
