from GenericBodyDialog import GenericBodyDialog
import dataStructures
import libraries


class CappedCylinderDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Capped Cylinder")

        self.groupBox_2.setTitle("Cylinder Start:")
        self.groupBox_3.setTitle("Cylinder End:")
        self.radius1Label.setText("Radius (cm):")
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self):
        # add to the shield dict
        shield = dataStructures.CappedCylinderShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.radius1 = self.radius1.text()
        shield.vector1 = [self.triplet1X.text(),
                           self.triplet1Y.text(),
                           self.triplet1Z.text()]
        shield.vector2 = [self.triplet2X.text(),
                           self.triplet2Y.text(),
                           self.triplet2Z.text()]
        libraries.shield_dict[shield.name] = shield

