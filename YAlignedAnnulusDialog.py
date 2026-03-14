from GenericBodyDialog import GenericBodyDialog


class YAlignedAnnulusDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Y-Aligned Infinite Annulus")

        self.groupBox_2.setTitle("Annulus Center:")
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Inner Radius (cm):")
        self.radius2Label.setText("Outer Radius (cm):")
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

