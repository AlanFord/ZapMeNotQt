import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QHeaderView, QStyledItemDelegate, QStyle
from PyQt6.QtCore import QFile, QIODeviceBase, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic
from PyQt6.QtGui import QColor

import libraries


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
        self.myModel = IsotopeModel()
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.setModel(self.myModel)
        self.accepted.connect(self.on_dialog_accepted)
        self.tableView.clicked.connect(self.myModel.toggle_isotope)
        self.tableView.setItemDelegate(DeselectedDelegate(self.tableView))

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

    def toggle_isotope(self, index):
        # check to see if it's a valid isotope
        entry = ((index.row()) * self.width) + index.column()
        if entry <= len(self.dataValues)-1:
            isotope_name = self.dataValues[entry]
            values = libraries.isotopes[isotope_name]
            libraries.isotopes[isotope_name] = [not values[0], values[1]]
            self.dataChanged.emit(index, index,
                                  [Qt.ItemDataRole.BackgroundRole,
                                   Qt.ItemDataRole.ForegroundRole])

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
        entry = ((index.row()) * self.width) + index.column()
        if entry > len(self.dataValues)-1:
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.dataValues[entry]
        if role == Qt.ItemDataRole.BackgroundRole:
            if libraries.isotopes[self.dataValues[entry]][0] is False:
                return QColor('white')
            else:
                return QColor('blue')
        if role == Qt.ItemDataRole.ForegroundRole:
            if libraries.isotopes[self.dataValues[entry]][0] is False:
                return QColor('black')
            else:
                return QColor('white')
