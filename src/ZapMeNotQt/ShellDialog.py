from .GenericBodyDialog import GenericBodyDialog
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


class ShellDialog(GenericBodyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Shell")

        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Thickness (cm):")
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        self.name_label.setVisible(False)
        self.name_field.setVisible(False)
        # hide any qtextedit fields that should not be validated
        self.triplet1X.hide()
        self.triplet1Y.hide()
        self.triplet1Z.hide()
        self.triplet2X.hide()
        self.triplet2Y.hide()
        self.triplet2Z.hide()
        self.radius2.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
