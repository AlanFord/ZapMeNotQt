from GenericBodyDialog import GenericBodyDialog
import dataStructures
from libraries import shield_dict


class XAlignedCylinderDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("X-Aligned Cylinder")

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

    def on_dialog_accepted(self):
        # add to the shield dict
        shield = dataStructures.XCylinderShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.radius1 = self.radius1.text()
        shield.radius2 = self.radius2.text()
        shield.vector1 = [self.triplet1X.text(),
                           self.triplet1Y.text(),
                           self.triplet1Z.text()]
        shield_dict[shield.name] = shield

