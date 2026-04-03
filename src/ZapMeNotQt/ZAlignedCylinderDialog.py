from GenericBodyDialog import GenericBodyDialog
import dataStructures
import libraries


class ZAlignedCylinderDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Z-Aligned Cylinder")

        self.groupBox_2.setTitle("Cylinder Center:")
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Length (cm):")
        self.radius2Label.setText("Radius (cm):")
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self):
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
        libraries.shield_dict[shield.name] = shield

