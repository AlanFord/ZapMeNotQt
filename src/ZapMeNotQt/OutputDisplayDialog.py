from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QDialogButtonBox

from ui.OutputDisplayDialog import Ui_Dialog

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


class OutputDisplayDialog(QDialog, Ui_Dialog):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setupUi(self)
        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        self.textEdit.setCurrentFont(fixed_font)
        self.textEdit.setText(text)
        buffer = self.textEdit.toMarkdown()
        self.textEdit.setMarkdown(buffer)
        self.buttonBox.accepted.connect(self.close)
