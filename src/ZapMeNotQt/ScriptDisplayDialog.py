import os

from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import QFile, QIODeviceBase
from PySide6.QtUiTools import QUiLoader
from pathlib import Path
''' '''
'''
ZapMeNotQt - a graphical user interface for ZapMeNot
Copyright (C) 2026  C. Alan Ford

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


class ScriptDisplayDialog(QDialog):
    def __init__(self, text_list: list[str]) -> None:
        super().__init__()
        self.load_ui()
        self.display_text = ""
        for entry in text_list:
            self.display_text += entry + "\n"
        self.textEdit.setText(self.display_text)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.saveFile)

    def load_ui(self) -> None:
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/script_display.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        loader = QUiLoader()
        loader.load(ui_file, self)
        ui_file.close()

    def saveFile(self) -> None:
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