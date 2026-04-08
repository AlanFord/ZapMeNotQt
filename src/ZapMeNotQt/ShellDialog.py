from GenericBodyDialog import GenericBodyDialog


class ShellDialog(GenericBodyDialog):
    def __init__(self):
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
