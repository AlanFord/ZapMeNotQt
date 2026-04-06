from GenericBodyDialog import GenericBodyDialog
from ShellDialog import ShellDialog
import dataStructures
from libraries import shield_dict


class SphereDialog(GenericBodyDialog):
    def __init__(self):
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

    def on_dialog_accepted(self):
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
        shield_dict[sphere.name] = sphere

    def the_shell_button_was_clicked(self):
        returnCode = self.shellDialog.exec()
        print("return code is ", returnCode)
        # if returnCode is PyQt6.QtWidgets.QDialog.accepted:
        if returnCode == 1:
            self.hasAShell = True
            self.shell = dataStructures.ShellShield()
            self.shell.density = self.shellDialog.density.text()
            self.shell.material = self.shellDialog.material.currentText()
            self.shell.thickness = self.shellDialog.radius1.text()

    def shellCheckBox_changed(self):
        if self.shellCheckBox.isChecked():
            self.shellButton.setEnabled(True)
        else:
            self.shellButton.setEnabled(False)

    def on_name_selected(self):
        super().on_name_selected()
        new_name = self.name_field.currentText()
        if new_name in shield_dict:
            existing_shield = shield_dict[new_name]
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
