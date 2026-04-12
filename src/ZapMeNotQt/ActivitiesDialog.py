import os
from pathlib import Path

from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QFile, QIODeviceBase, \
    QAbstractTableModel, QModelIndex, Qt
from PyQt6 import uic

import libraries


class ActivitiesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.myModel = ActivityModel()
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
    def __init__(self):
        super().__init__()

    def rowCount(self, parent=QModelIndex()):
        return 6

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return 1
