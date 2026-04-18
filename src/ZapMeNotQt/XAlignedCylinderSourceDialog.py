from XAlignedCylinderDialog import XAlignedCylinderDialog
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


class XAlignedCylinderSourceDialog(XAlignedCylinderDialog):
    def __init__(self) -> None:
        super().__init__()
        self.name_field.hide()
        self.name_label.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

    def on_dialog_accepted(self) -> None:
        source = dataStructures.XCylinderSource()
        source.material = self.material.currentText()
        source.density = self.density.text()
        source.radius1 = self.radius1.text()
        source.radius2 = self.radius2.text()
        source.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        libraries.source = source
