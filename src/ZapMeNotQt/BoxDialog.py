from GenericBodyDialog import GenericBodyDialog
import dataStructures
from libraries import shield_dict


class BoxDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Box")

        self.groupBox_2.setTitle("Box Center:")
        self.groupBox_3.setTitle("Box Dimensions:")
        self.radius1.setVisible(False)
        self.radius1Label.setVisible(False)
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        # hide any qtextedit fields that should not be validated
        self.radius1.hide()
        self.radius2.hide()
        # change the validators
        self.radius1.setValidator(self.double_validator)
        self.triplet2X.setValidator(self.positive_validator)
        self.triplet2Y.setValidator(self.positive_validator)
        self.triplet2Z.setValidator(self.positive_validator)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self):
        # add to the shield dict
        shield = dataStructures.BoxShield()
        shield.name = self.name_field.currentText()
        shield.material = self.material.currentText()
        shield.density = self.density.text()
        shield.vector1 = [self.triplet1X.text(),
                           self.triplet1Y.text(),
                           self.triplet1Z.text()]
        shield.vector2 = [self.triplet2X.text(),
                           self.triplet2Y.text(),
                           self.triplet2Z.text()]
        shield_dict[shield.name] = shield
