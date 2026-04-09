from BoxDialog import BoxDialog
import dataStructures
import libraries


class BoxSourceDialog(BoxDialog):
    def __init__(self):
        super().__init__()
        self.name_field.hide()
        self.name_label.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

    def on_dialog_accepted(self):
        source = dataStructures.BoxSource()
        source.material = self.material.currentText()
        source.density = self.density.text()
        source.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        source.vector2 = [self.triplet2X.text(),
                          self.triplet2Y.text(),
                          self.triplet2Z.text()]
        libraries.source = source
