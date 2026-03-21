from GenericBodyDialog import GenericBodyDialog


class CappedCylinderDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Capped Cylinder")

        self.groupBox_2.setTitle("Cylinder Start:")
        self.groupBox_3.setTitle("Cylinder End:")
        self.radius1Label.setText("Radius (cm):")
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

