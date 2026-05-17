from PyQt6.QtWidgets import QDialog
from .GenericBodyDialog import GenericBodyDialog
from .ShellDialog import ShellDialog
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


class SphereDialog(GenericBodyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Sphere")

        self.groupBox_2.setTitle("Sphere Center:")
        self.radius1Label.setText("Radius (cm):")
        self.shellCheckBox.setVisible(True)
        self.shellButton.setVisible(True)
        self.radius2Label.setVisible(False)
        self.groupBox_3.setVisible(False)
        # hide any qtextedit fields that should not be validated
        self.triplet2X.hide()
        self.triplet2Y.hide()
        self.triplet2Z.hide()
        self.radius2.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.hasAShell = False
        self.shell = None
        self.shellButton.clicked.connect(self.the_shell_button_was_clicked)
        self.shellCheckBox.stateChanged.connect(self.shellCheckBox_changed)
        self.shellDialog = ShellDialog()
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        # add to the shield dict
        sphere = dataStructures.SphereShield()
        sphere.name = self.name_field.currentText()
        sphere.material = self.material.currentText()
        sphere.density = self.density.text()
        sphere.radius1 = self.radius1.text()
        sphere.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        if self.hasAShell:
            sphere.shell = self.shell
        else:
            sphere.shell = None
        libraries.model.shield_dict[sphere.name] = sphere

    def the_shell_button_was_clicked(self) -> None:
        if self.shellDialog.exec() == QDialog.DialogCode.Accepted:
            self.hasAShell = True
            self.shell = dataStructures.ShellShield()
            self.shell.density = self.shellDialog.density.text()
            self.shell.material = self.shellDialog.material.currentText()
            self.shell.thickness = self.shellDialog.radius1.text()

    def shellCheckBox_changed(self) -> None:
        if self.shellCheckBox.isChecked():
            self.shellButton.setEnabled(True)
        else:
            self.shellButton.setEnabled(False)

    # override on_name_selected to include the sphere shell
    def on_name_selected(self) -> None:
        super().on_name_selected()
        new_name = self.name_field.currentText()
        if new_name in libraries.model.shield_dict:
            existing_shield = libraries.model.shield_dict[new_name]
            # loading the existing shield data into the dialog
            if existing_shield.shell is not None:
                index = self.shellDialog.material.findText(
                    existing_shield.material)
                if index != -1:
                    self.shellDialog.material.setCurrentIndex(index)
                self.shellDialog.density.setText(existing_shield.shell.density)
                self.shellDialog.radius1.setText(
                    existing_shield.shell.thickness)
                self.shellCheckBox.setChecked(True)
            else:
                self.shellCheckBox.setChecked(False)
