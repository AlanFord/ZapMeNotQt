import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QFile, QIODeviceBase, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic

import libraries


class ActivitiesDialog(QDialog):
    def __init__(self, master_library):
        super().__init__()
        self.load_ui()
        self.myModel = ActivityModel(master_library)
        self.tableView.setModel(self.myModel)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/ActivitiesDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        pass


class ActivityModel(QAbstractTableModel):
    def __init__(self, master_library):
        super().__init__()
        self._data = master_library.loc[master_library['active']]
        self._data = self._data.drop("active", axis=1)

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
        # TODO: don't set activities in libraries.isotopes if cancel button
        # is selected!
        if role == Qt.ItemDataRole.EditRole:
            # Validate input here
            if self.isValid(value):
                self._data.iloc[index.row(), index.column()] = float(value)
                # isotope_name = self._data.index[index.row()]
                # libraries.isotopes.loc[isotope_name, 'activity'] = float(value)
                return True
            else:
                return False

    def isValid(self, value):
        try:
            float(value)
        except ValueError:
            return False
        else:
            return True
