import PySide6.QtWidgets

from ui.OptionsProgenyDialog import Ui_Dialog

import libraries
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


class OptionsProgenyDialog(PySide6.QtWidgets.QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.checkBox.setChecked(libraries.progeny)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        libraries.progeny = self.checkBox.isChecked()
