from GenericBodyDialog import GenericBodyDialog
import dataStructures
import libraries


class LineSourceDialog(GenericBodyDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line")

        self.name_field.setVisible(False)
        self.name_label.setVisible(False)
        self.groupBox.setVisible(False)
        self.groupBox_2.setTitle("Starting Location:")
        self.groupBox_3.setTitle("Ending Location:")
        self.radius1.setVisible(False)
        self.radius1Label.setVisible(False)
        self.radius2.setVisible(False)
        self.radius2Label.setVisible(False)
        # hide any qtextedit fields that should not be validated
        self.density.hide()
        self.radius1.hide()
        self.radius2.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self):
        source = dataStructures.LineSource()
        source.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        source.vector2 = [self.triplet2X.text(),
                          self.triplet2Y.text(),
                          self.triplet2Z.text()]
        libraries.source = source
