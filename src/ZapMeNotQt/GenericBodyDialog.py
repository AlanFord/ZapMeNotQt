import os

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase, QRegularExpression
from PyQt6 import uic
from PyQt6.QtGui import QValidator, QDoubleValidator, \
    QRegularExpressionValidator
from pathlib import Path

from libraries import materials, shield_dict


class GenericBodyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.material.addItems(materials.keys())
        self.material.setCurrentIndex(0)
        self.density.setText(str(materials[self.material.currentText()]))
        self.material.currentIndexChanged.connect(self.on_material_selected)
        self.name_field.currentIndexChanged.connect(self.on_name_selected)
        self.name_field.addItems(shield_dict.keys())
        # set the shell features to not visible as most dialogs won't use these
        self.shellCheckBox.setVisible(False)
        self.shellButton.setVisible(False)
        # validators
        # TODO: improve the regex to accept strings with embedded whitespace
        self.name_validator = QRegularExpressionValidator(
            QRegularExpression('[^\\s]+'), self)
        self.double_validator = QDoubleValidator(self)
        self.positive_validator = QDoubleValidator(self)
        self.positive_validator.setBottom(0)
        self.density.setValidator(self.positive_validator)
        self.radius1.setValidator(self.positive_validator)
        self.radius2.setValidator(self.positive_validator)
        self.triplet1X.setValidator(self.double_validator)
        self.triplet1Y.setValidator(self.double_validator)
        self.triplet1Z.setValidator(self.double_validator)
        self.triplet2X.setValidator(self.double_validator)
        self.triplet2Y.setValidator(self.double_validator)
        self.triplet2Z.setValidator(self.double_validator)

        # self.buttonBox.accepted.disconnect(self.accept)
        # self.buttonBox.accepted.connect(self.validate_doubles)

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

    def accept(self):
        # first check the QTextFields for properly formatted
        #   numbers.  Then, if the shield name field is visible,
        #   check for a valid shield name.  Call the dialog
        #   accept method only if all fields are valid.
        try:
            for field in [
                            self.triplet1X, self.triplet1Y, self.triplet1Z,
                            self.triplet2X, self.triplet2Y, self.triplet2Z,
                            self.radius1, self.radius2, self.density]:
                if not field.isHidden():
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
            if self.name_field.isVisible():
                rcode = self.name_validator.validate(
                    self.name_field.currentText(), 0)
                if rcode[0] == QValidator.State.Acceptable:
                    super().accept()
                else:
                    QMessageBox.critical(self, "Error",
                                    "Please enter a name for the new shield" +
                                    " or select an existing name to modify " +
                                    "a shield.  White space not allowed.")
            else:
                super().accept()
