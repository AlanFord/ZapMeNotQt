from GenericBodyDialog import GenericBodyDialog


class AnnulusShieldDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infinite Annulus")

        self.groupBox_2.setTitle("Annulus Center:")
        self.groupBox_3.setTitle("Annulus Axis:")
        self.radius1Label.setText("Inner Radius (cm):")
        self.radius2Label.setText("Outer Radius (cm):")
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        