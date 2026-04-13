import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic
from PyQt6.QtGui import QValidator, QDoubleValidator


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

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/ActivitiesDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
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
                self._data.iloc[index.row(), index.column()] = float(value)
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
