import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
from DetectorLocationDialog import DetectorDialog
from OptionsGroupsDialog import OptionsGroupsDialog
from OptionsProgenyDialog import OptionsProgenyDialog
from OptionsBuildupDialog import OptionsBuildupDialog
from BoxShieldDialog import BoxShieldDialog
from SphereShieldDialog import SphereShieldDialog
from XSlabShieldDialog import XSlabShieldDialog


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

        # shield menu setup
        self.BoxShieldDialog = BoxShieldDialog()
        self.actionBox.triggered.connect(self.BoxShieldDialog.exec)
        self.SphereShieldDialog = SphereShieldDialog()
        self.actionSphere.triggered.connect(self.SphereShieldDialog.exec)
        self.XSlabShieldDialog = XSlabShieldDialog()
        self.actionSemiInfiniteXSlab.triggered.connect(self.XSlabShieldDialog.exec)

        # options menu setup
        self.OptionsGroupsDialog = OptionsGroupsDialog()
        self.actionEnergy_Groups.triggered.connect(self.OptionsGroupsDialog.exec)
        self.OptionsProgenyDialog = OptionsProgenyDialog()
        self.actionDaughters.triggered.connect(self.OptionsProgenyDialog.exec)
        self.OptionsBuildupDialog = OptionsBuildupDialog()
        self.actionBuildup_Material.triggered.connect(self.OptionsBuildupDialog.exec)
        
        # detector menu setup
        self.detectorDialog = DetectorDialog()
        self.location.triggered.connect(self.detectorDialog.exec)
        self.summaryDescription.setPlainText("Nothing to see, Folks!")

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/MainWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
