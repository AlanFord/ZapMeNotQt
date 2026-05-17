from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt6.QtGui import QValidator, QDoubleValidator

from .ui.PhotonsDialog import Ui_Dialog

from . import libraries
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


class PhotonDialog(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._data = libraries.model.photons  # list of lists
        if len(self._data) == 0:
            self._data = [["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""],
                          ["", ""]]

        self.myModel = PhotonModel(self._data, self)
        self.tableView.setModel(self.myModel)
        self.tableView.verticalHeader().setVisible(False)
        self.accepted.connect(self.on_dialog_accepted)

    def on_dialog_accepted(self) -> None:
        # copy entries back into permanent storage
        libraries.model.photons = self._data

# =================================================================


class PhotonModel(QAbstractTableModel):
    def __init__(self, data, parent):
        super().__init__()
        self._data = data
        self.positive_validator = QDoubleValidator(self)
        self.positive_validator.setBottom(0)
        self.headers = ["Photon (MeV)", "Intensity ()"]
        self.parent = parent

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole or \
                role == Qt.ItemDataRole.EditRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Vertical:
                return section
            if orientation == Qt.Orientation.Horizontal:
                if section == 0:
                    return 'Energy (MeV)'
                else:
                    return 'Intensity (photon/sec)'

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | \
            Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role):
        HIGH = 15    # upper photon energy limit
        LOW = 0.015  # lower photon energy limit
        if role == Qt.ItemDataRole.EditRole:
            # ignore a row that is all empty strings
            if self._data[index.row()] == ["", ""] and value == "":
                return True
            elif not self.isValid(value):
                # screen out badly-formatted numbers
                if value == "":
                    insert = "A blank field"
                else:
                    insert = value
                QMessageBox.critical(self.parent, "Error",
                                     insert + " is an invalid activity.")
                return False
            else:
                # check for energy out of range
                energy = float(value)
                if index.column() == 0:
                    if energy < LOW or energy > HIGH:
                        QMessageBox.critical(self.parent, "Error",
                                             "Photon energy is out of range.")
                        return False
                self._data[index.row()][index.column()] = value
                return True

    def isValid(self, value):
        results = self.positive_validator.validate(value, 0)
        if results[0] == QValidator.State.Acceptable:
            return True
        else:
            return False
