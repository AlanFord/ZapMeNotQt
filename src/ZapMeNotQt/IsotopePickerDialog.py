from PyQt6.QtWidgets import QDialog, QHeaderView, QStyledItemDelegate, \
    QStyle, QMessageBox
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt6.QtGui import QColor

from .ui.IsotopeSelector import Ui_Dialog

from . import dataStructures
from .ActivitiesDialog import ActivitiesDialog
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


class DeselectedDelegate(QStyledItemDelegate):
    # this delegate turns off the highlighting of selected
    # QTableView cells, allowing the background color to be
    # displayed
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.state &= ~QStyle.StateFlag.State_Selected


class IsotopePickerDialog(QDialog, Ui_Dialog):
    def __init__(self, model: dataStructures.Model) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = model
        # create a working copy, distinct from the argument instance
        self.isotope_library = model.isotopes.copy()
        self.myModel = IsotopeModel(self.isotope_library, self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.setModel(self.myModel)
        self.tableView.clicked.connect(self.myModel.toggle_isotope)
        self.tableView.setItemDelegate(DeselectedDelegate(self.tableView))
        self.accepted.connect(self.on_dialog_accepted)
        self.pushButton.clicked.connect(self.open_activities)

    def on_dialog_accepted(self) -> None:
        # copy the isotope_library back into the production library
        # this will not happen if the cancel button is used
        self.model.isotopes = self.isotope_library.copy()

    def open_activities(self) -> None:
        # ensure that isotopes are selected before calling
        # the activities dialog
        data = self.isotope_library.loc[self.isotope_library['active']]
        if data.shape[0] == 0:
            QMessageBox.critical(self, "Error",
                                 "Please select at least one isotope" +
                                 "prior to specifying activities.")
        else:
            second_dialog = ActivitiesDialog(data, self.model)
            second_dialog.exec()
            for index in data.index:
                self.isotope_library.at[index, 'activity'] = data.loc[
                    index, 'activity']


class IsotopeModel(QAbstractTableModel):
    def __init__(self, isotope_library, model: dataStructures.Model):
        super().__init__()
        self.width = 5
        self.displayValues = model.isotopes.index.to_list()
        self.isotope_library = isotope_library

    def toggle_isotope(self, index) -> None:
        # check to see if it's a valid isotope
        entry = ((index.row()) * self.width) + index.column()
        if entry <= len(self.displayValues)-1:
            isotope_name = self.displayValues[entry]
            self.isotope_library.at[isotope_name, 'active'] = \
                not self.isotope_library.loc[isotope_name, 'active']
            # clear the activity if isotope is unselected
            if not self.isotope_library.at[isotope_name, 'active']:
                self.isotope_library.loc[isotope_name, 'activity'] = \
                    '0.0'
            self.dataChanged.emit(index, index,
                                  [Qt.ItemDataRole.BackgroundRole,
                                   Qt.ItemDataRole.ForegroundRole])

    def rowCount(self, parent=QModelIndex()):
        # Return the total number of rows in the model
        base = len(self.displayValues) // self.width
        if (len(self.displayValues) % self.width) > 0:
            return base + 1
        else:
            return base

    def columnCount(self, parent=QModelIndex()):
        return self.width

    def data(self, index, role):
        entry = ((index.row()) * self.width) + index.column()
        if entry > len(self.displayValues)-1:
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.displayValues[entry]
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.isotope_library.loc[self.displayValues[entry], 'active']:
                return QColor('blue')
            else:
                return QColor('white')
        if role == Qt.ItemDataRole.ForegroundRole:
            if self.isotope_library.loc[self.displayValues[entry], 'active']:
                return QColor('white')
            else:
                return QColor('black')
