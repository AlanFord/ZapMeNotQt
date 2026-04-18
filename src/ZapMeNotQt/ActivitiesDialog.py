import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic
from PyQt6.QtGui import QValidator, QDoubleValidator

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


class ActivitiesDialog(QDialog):
    def __init__(self, master_library):
        super().__init__()
        self.load_ui()
        self.master_library = master_library
        self._data = self.master_library.loc[self.master_library['active']]
        self._data = self._data.drop("active", axis=1)

        self.myModel = ActivityModel(self._data, self)
        self.tableView.setModel(self.myModel)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self) -> None:
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/ActivitiesDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self) -> None:
        # record the activity units
        if self.radioButton.isChecked():
            libraries.activity_type = libraries.Activity_Type.Curie
        else:
            libraries.activity_type = libraries.Activity_Type.Becquerel

        # copy entries from self._data to self.master_library
        for index in self._data.index:
            self.master_library.at[index, 'activity'] = self._data.loc[
                index, 'activity']

# =================================================================


class ActivityModel(QAbstractTableModel):
    def __init__(self, data, parent):
        super().__init__()
        self.parent = parent
        self._data = data
        self.positive_validator = QDoubleValidator(self)
        self.positive_validator.setBottom(0)

    def rowCount(self, parent=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return self._data.shape[1]

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole or \
                role == Qt.ItemDataRole.EditRole:
            return self._data.iloc[index.row(), index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])
            if orientation == Qt.Orientation.Horizontal:
                return 'Activity'

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | \
            Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self.isValid(value):
                self._data.iloc[index.row(), index.column()] = value
                return True
            else:
                if value == "":
                    insert = "A blank field"
                else:
                    insert = value
                QMessageBox.critical(self.parent, "Error",
                                     insert + " is an invalid activity.")
                return False

    def isValid(self, value):
        results = self.positive_validator.validate(value, 0)
        if results[0] == QValidator.State.Acceptable:
            return True
        else:
            return False
