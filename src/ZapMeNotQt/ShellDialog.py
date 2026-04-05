from GenericBodyDialog import GenericBodyDialog


class ShellDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shell")

        self.groupBox_2.setVisible(False)
        self.groupBox_3.setVisible(False)
        self.radius1Label.setText("Thickness (cm):")
        # change the validator
        self.radius1.setValidator(self.positive_validator)
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        self.name_label.setVisible(False)
        self.name_field.setVisible(False)
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

