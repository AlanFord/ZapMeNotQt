from GenericBodyDialog import GenericBodyDialog
from ShellDialog import ShellDialog


class SphereDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sphere")

        self.groupBox_2.setTitle("Sphere Center:")
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Radius (cm):")
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

