from GenericBodyDialog import GenericBodyDialog
import dataStructures
from libraries import shield_dict
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


class ZAlignedCylinderDialog(GenericBodyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Z-Aligned Cylinder")

        self.groupBox_2.setTitle("Cylinder Center:")
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Length (cm):")
        self.radius2Label.setText("Radius (cm):")
        # hide any qtextedit fields that should not be validated
        self.triplet2X.hide()
        self.triplet2Y.hide()
        self.triplet2Z.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        # add to the shield dict
        shield = dataStructures.ZCylinderShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.radius1 = self.radius1.text()
        shield.radius2 = self.radius2.text()
        shield.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        shield_dict[shield.name] = shield
