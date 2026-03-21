from GenericBodyDialog import GenericBodyDialog


class XAlignedCylinderDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("X-Aligned Cylinder")

        self.groupBox_2.setTitle("Cylinder Center:")
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Length (cm):")
        self.radius2Label.setText("Radius (cm):")
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

