import PyQt6.QtWidgets
from GenericBodyDialog import GenericBodyDialog
from ShellDialog import ShellDialog
import dataStructures
import libraries


class SphereDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sphere")

        self.groupBox_2.setTitle("Sphere Center:")
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Radius (cm):")
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.ShellDialog = ShellDialog()
        self.shell = None
        self.shellButton.clicked.connect(self.the_button_was_clicked)
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
        sphere.shell = self.shell
        libraries.shield_dict[sphere.name] = sphere

    def the_button_was_clicked(self):
        returnCode = self.ShellDialog.exec()
        print("return code is ", returnCode)
        # if returnCode is PyQt6.QtWidgets.QDialog.accepted:
        if returnCode == 1:
            self.shell = dataStructures.ShellShield()
            self.shell.density = self.ShellDialog.density.text()
            self.shell.material = self.ShellDialog.material.currentText()
            self.shell.thickness = self.ShellDialog.radius1.text()
        
