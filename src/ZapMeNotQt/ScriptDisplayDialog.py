from PyQt6.QtWidgets import QDialog, QFileDialog, QDialogButtonBox, QPushButton

from ui.script_display import Ui_Dialog

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


class ScriptDisplayDialog(QDialog, Ui_Dialog):
    def __init__(self, text_list: list[str]) -> None:
        super().__init__()
        self.setupUi(self)
        self.display_text = ""
        # TODO: replace this with the concatenation method used before "exec()"
        for entry in text_list:
            self.display_text += entry + "\n"
        self.textEdit.setText(self.display_text)
        self.buttonBox.accepted.connect(self.close)
        # add a "Save" button to the buttonBox that will allow user to save the script
        self.save_file_button = QPushButton("Save ...", self)
        self.buttonBox.addButton(self.save_file_button, 
                            QDialogButtonBox.ButtonRole.ActionRole)
        self.buttonBox.clicked.connect(self.saveFile)



    def saveFile(self,button) -> None:
        if button is self.save_file_button:
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
