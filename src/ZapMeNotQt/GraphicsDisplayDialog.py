import os

from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
import pyvista as pv
from pathlib import Path
from zapmenot import model, source, shield, detector, material
import libraries
import dataStructures
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


class GraphicsDisplayDialog(QDialog):
    def __init__(self, text_list: str) -> None:
        super().__init__()
        self.load_ui()
        # build a stripped-down ZapMeNot model sufficient for display
        self.my_model = model.Model()
        if libraries.detector is not None:
            local_detector = libraries.detector.phalax()
            self.my_model.add_detector(local_detector)

        for shield_name in libraries.shield_dict.keys():
            local_shield_list = libraries.shield_dict[shield_name].phalax()
            for local_shield in local_shield_list:
                self.my_model.add_shield(local_shield)

        if libraries.source is not None:
            local_source_list = libraries.source.phalax()
            for local_source in local_source_list:
                if isinstance(local_source, shield.Shell):
                    self.my_model.add_shield(local_source)
                if isinstance(local_source, source.Source):
                    self.my_model.add_source(local_source)

        self.my_model._build_image(self.display_view)
        self.pushButton.clicked.connect(self.close)
        # self.pushButton_2.clicked.connect(self.saveFile)

    def load_ui(self) -> None:
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/GraphicsDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
