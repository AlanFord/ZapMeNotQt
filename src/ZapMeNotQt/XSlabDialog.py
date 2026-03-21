from GenericBodyDialog import GenericBodyDialog


class XSlabDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semi-infinite X Slab")

        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("X-start (cm):")
        self.radius2Label.setText("X-end (cm):")
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
