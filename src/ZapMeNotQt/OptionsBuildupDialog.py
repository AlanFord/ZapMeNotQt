import os

import PySide6.QtWidgets
from PySide6.QtCore import QFile, QIODeviceBase
from PySide6.QtUiTools import QUiLoader
from pathlib import Path
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


class OptionsBuildupDialog(PySide6.QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.load_ui()
        self.comboBox.addItems(libraries.buildup_factor_materials)
        if libraries.buildup_material != "None":
            index = self.comboBox.findText(libraries.buildup_material)
            if index != -1:
                self.comboBox.setCurrentIndex(index)
            else:
                self.comboBox.setCurrentIndex(0)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self) -> None:
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/OptionsBuildupDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        loader = QUiLoader()
        loader.load(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self) -> None:
        libraries.buildup_material = self.comboBox.currentText()
