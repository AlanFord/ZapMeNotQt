import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QHeaderView, QStyledItemDelegate, \
    QStyle, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic
from PyQt6.QtGui import QColor

import libraries
from ActivitiesDialog import ActivitiesDialog


class DeselectedDelegate(QStyledItemDelegate):
    # this delegate turns off the highlighting of selected
    # QTableView cells, allowing the background color to be
    # displayed
    def initStyleOption(self, opt, index):
        super().initStyleOption(opt, index)
        opt.state &= ~QStyle.StateFlag.State_Selected


class IsotopePickerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.library_copy = libraries.isotopes.copy()
        self.myModel = IsotopeModel(self.library_copy)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.setModel(self.myModel)
        self.tableView.clicked.connect(self.myModel.toggle_isotope)
        self.tableView.setItemDelegate(DeselectedDelegate(self.tableView))
        self.accepted.connect(self.on_dialog_accepted)
        self.pushButton.clicked.connect(self.open_activities)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/IsotopeSelector.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        # copy the library_copy back into the production library
        # this will not happen if the cancel button is used
        libraries.isotopes = self.library_copy.copy()

    def open_activities(self):
        # ensure that isotopes are selected before calling
        # the activities dialog
        data = self.library_copy.loc[self.library_copy['active']]
        if data.shape[0] == 0:
            QMessageBox.critical(self, "Error",
                                 "Please select at least one isotope" +
                                 "prior to specifying activities.")
        else:
            second_dialog = ActivitiesDialog(data)
            second_dialog.exec()
            for index in data.index:
                self.library_copy.at[index, 'activity'] = data.loc[
                    index, 'activity']


class IsotopeModel(QAbstractTableModel):
    def __init__(self, local_library):
        super().__init__()
        self.width = 5
        self.displayValues = libraries.isotopes.index.to_list()
        self.local_library = local_library

    def toggle_isotope(self, index):
        # check to see if it's a valid isotope
        entry = ((index.row()) * self.width) + index.column()
        if entry <= len(self.displayValues)-1:
            isotope_name = self.displayValues[entry]
            self.local_library.at[isotope_name, 'active'] = \
                not self.local_library.loc[isotope_name, 'active']
            # clear the activity if isotope is unselected
            if not self.local_library.at[isotope_name, 'active']:
                self.local_library.loc[isotope_name, 'activity'] = \
                    0.0
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
            if self.local_library.loc[self.displayValues[entry], 'active']:
                return QColor('blue')
            else:
                return QColor('white')
        if role == Qt.ItemDataRole.ForegroundRole:
            if self.local_library.loc[self.displayValues[entry], 'active']:
                return QColor('white')
            else:
                return QColor('black')
