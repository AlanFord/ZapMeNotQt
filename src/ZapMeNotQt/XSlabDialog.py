from GenericBodyDialog import GenericBodyDialog
import dataStructures
import libraries


class XSlabDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semi-infinite X Slab")

        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("X-start (cm):")
        self.radius2Label.setText("X-end (cm):")
        # change the validators
        self.radius1.setValidator(self.double_validator)
        self.radius2.setValidator(self.double_validator)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self):
        # add to the shield dict
        shield = dataStructures.XSlabShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.radius1 = self.radius1.text()
        shield.radius2 = self.radius2.text()
        libraries.shield_dict[shield.name] = shield
