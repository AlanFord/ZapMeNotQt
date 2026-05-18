from PyQt6.QtWidgets import QDialog
import zapmenot.model
import zapmenot.source
import zapmenot.shield
#from zapmenot import model, source, shield

from .ui.GraphicsDialog import Ui_GraphicsDialog

from . import dataStructures
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


class GraphicsDisplayDialog(QDialog, Ui_GraphicsDialog):
    def __init__(self, text_list: str, data_model: dataStructures.Model) -> None:
        super().__init__()
        self.setupUi(self)
        # build a stripped-down ZapMeNot model sufficient for display
        self.shielding_model = zapmenot.model.Model()
        if data_model.detector is not None:
            local_detector = data_model.detector.display_code()
            self.shielding_model.add_detector(local_detector)

        for shield_name in data_model.shield_dict.keys():
            local_shield_list = data_model.shield_dict[shield_name].display_code()
            for local_shield in local_shield_list:
                self.shielding_model.add_shield(local_shield)

        if data_model.source is not None:
            local_source_list = data_model.source.display_code()
            for local_source in local_source_list:
                if isinstance(local_source, zapmenot.shield.Shell):
                    self.shielding_model.add_shield(local_source)
                if isinstance(local_source, zapmenot.source.Source):
                    self.shielding_model.add_source(local_source)

        self.shielding_model._build_image(self.display_view)
        self.pushButton.clicked.connect(self.close)
        # self.pushButton_2.clicked.connect(self.saveFile)
