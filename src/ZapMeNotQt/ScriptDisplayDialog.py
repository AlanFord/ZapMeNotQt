import os

from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path


class ScriptDisplayDialog(QDialog):
    def __init__(self, text_list):
        super().__init__()
        self.load_ui()
        self.display_text = ""
        for entry in text_list:
            self.display_text += entry + "\n"
        self.textEdit.setText(self.display_text)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.saveFile)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/script_display.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def saveFile(self):
        # Open the save file dialog
        filename, _ = QFileDialog.getSaveFileName(None, 
                                                  "Save File", 
                                                  "", 
                                                  "Python Files (*.py);;All Files (*)")

        if filename:
            # Proceed to save the file using the selected filename
            with open(filename, 'w') as file:
                file.write(self.display_text)
            file.close()