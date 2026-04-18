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


class PointSourceDialog(GenericBodyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Point")

        self.name_field.setVisible(False)
        self.name_label.setVisible(False)
        self.groupBox.setVisible(False)
        self.groupBox_2.setTitle("Location:")
        self.groupBox_3.setVisible(False)
        self.radius1.setVisible(False)
        self.radius1Label.setVisible(False)
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        # hide any qtextedit fields that should not be validated
        self.density.hide()
        self.triplet2X.hide()
        self.triplet2Y.hide()
        self.triplet2Z.hide()
        self.radius1.hide()
        self.radius2.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        source = dataStructures.PointSource()
        source.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        libraries.source = source
