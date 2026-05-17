from .GenericBodyDialog import GenericBodyDialog
from PyQt6.QtWidgets import QMessageBox
from . import dataStructures
from . import libraries
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


class XSlabDialog(GenericBodyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Semi-infinite X Slab")

        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("X-start (cm):")
        self.radius2Label.setText("X-end (cm):")
        # hide any qtextedit fields that should not be validated
        self.triplet1X.hide()
        self.triplet1Y.hide()
        self.triplet1Z.hide()
        self.triplet2X.hide()
        self.triplet2Y.hide()
        self.triplet2Z.hide()

        # change the validators
        self.radius1.setValidator(self.double_validator)
        self.radius2.setValidator(self.double_validator)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        # add to the shield dict
        shield = dataStructures.XSlabShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.radius1 = self.radius1.text()
        shield.radius2 = self.radius2.text()
        libraries.model.shield_dict[shield.name] = shield

    def accept(self) -> None:
        if float(self.radius2.text()) <= float(self.radius1.text()):
            # X-end should be larger than X-start
            QMessageBox.critical(self, "Error",
                                 "X-end must be larger than X-start")
        else:
            super().accept()
