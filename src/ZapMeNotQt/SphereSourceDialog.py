from SphereDialog import SphereDialog
import dataStructures
import libraries


class SphereSourceDialog(SphereDialog):
    def __init__(self):
        super().__init__()
        self.name_field.hide()
        self.name_label.hide()
        # shrink the height of the dialog to fit the visible widgets
        self.resize(self.size().width(), 4)

    def on_dialog_accepted(self):
        source = dataStructures.SphereSource()
        source.material = self.material.currentText()
        source.density = self.density.text()
        source.radius1 = self.radius1.text()
        source.vector1 = [self.triplet1X.text(),
                          self.triplet1Y.text(),
                          self.triplet1Z.text()]
        if self.hasAShell:
            source.shell = self.shell
        else:
            source.shell = None
        libraries.source = source
