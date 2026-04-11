import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PyQt6.QtCore import QFile, QIODeviceBase, QRegularExpression, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic

import libraries


class IsotopePickerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.myModel = IsotopeModel()
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.setModel(self.myModel)
        self.accepted.connect(self.on_dialog_accepted)

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent /
                         "ui/IsotopeSelector.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def on_dialog_accepted(self):
        pass


class IsotopeModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.width = 5
        self.dataValues = list(libraries.isotopes.keys())

    def rowCount(self, parent=QModelIndex()):
        # Return the total number of rows in the model
        base = len(libraries.isotopes) // self.width
        if (len(libraries.isotopes) % self.width) > 0:
            return base + 1
        else:
            return base

    def columnCount(self, parent=QModelIndex()):
        return self.width

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            entry = ((index.row()) * self.width) + index.column()
            if entry > len(self.dataValues)-1:
                return None
            else:
                return self.dataValues[entry]

    # def headerData(self, section, orientation, role):
    #     pass
