from GenericBodyDialog import GenericBodyDialog
import dataStructures
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


class AnnulusDialog(GenericBodyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Infinite Annulus")

        self.groupBox_2.setTitle("Annulus Center:")
        self.groupBox_3.setTitle("Annulus Axis:")
        self.radius1Label.setText("Inner Radius (cm):")
        self.radius2Label.setText("Outer Radius (cm):")
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        # add to the shield dict
        shield = dataStructures.AnnulusShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.radius1 = self.radius1.text()
        shield.radius2 = self.radius2.text()
        shield.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        shield.vector2 = [self.triplet2X.text(),
                          self.triplet2Y.text(),
                          self.triplet2Z.text()]
        libraries.model.shield_dict[shield.name] = shield
