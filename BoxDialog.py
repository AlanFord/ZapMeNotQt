from GenericBodyDialog import GenericBodyDialog


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
        self.shellButton.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

