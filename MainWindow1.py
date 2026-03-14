import os

import PyQt6.QtWidgets
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
from DetectorLocationDialog import DetectorDialog
from OptionsGroupsDialog import OptionsGroupsDialog
from OptionsProgenyDialog import OptionsProgenyDialog
from OptionsBuildupDialog import OptionsBuildupDialog
from BoxDialog import BoxDialog
from SphereDialog import SphereDialog
from XSlabDialog import XSlabDialog
from AnnulusDialog import AnnulusDialog
from CappedCylinderDialog import CappedCylinderDialog
from XAlignedCylinderDialog import XAlignedCylinderDialog
from YAlignedCylinderDialog import YAlignedCylinderDialog
from ZAlignedCylinderDialog import ZAlignedCylinderDialog
from XAlignedAnnulusDialog import XAlignedAnnulusDialog
from YAlignedAnnulusDialog import YAlignedAnnulusDialog
from ZAlignedAnnulusDialog import ZAlignedAnnulusDialog


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

        # shield menu setup
        self.BoxShieldDialog = BoxDialog()
        self.actionBox.triggered.connect(self.BoxShieldDialog.exec)
        self.SphereShieldDialog = SphereDialog()
        self.actionSphere.triggered.connect(self.SphereShieldDialog.exec)
        self.XSlabShieldDialog = XSlabDialog()
        self.actionSemiInfiniteXSlab.triggered.connect(self.XSlabShieldDialog.exec)
        self.AnnulusDialog = AnnulusDialog()
        self.actionInfiniteAnnulus.triggered.connect(self.AnnulusDialog.exec)
        self.CappedCylinderDialog = CappedCylinderDialog()
        self.actionCappedCylinder.triggered.connect(self.CappedCylinderDialog.exec)
        self.XAlignedCylinderDialog = XAlignedCylinderDialog()
        self.actionX_Aligned_Cylinder.triggered.connect(self.XAlignedCylinderDialog.exec)
        self.YAlignedCylinderDialog = YAlignedCylinderDialog()
        self.actionY_Aligned_Cylinder.triggered.connect(self.YAlignedCylinderDialog.exec)
        self.ZAlignedCylinderDialog = ZAlignedCylinderDialog()
        self.actionZ_Aligned_Cylinder.triggered.connect(self.ZAlignedCylinderDialog.exec)
        self.XAlignedAnnulusDialog = XAlignedAnnulusDialog()
        self.actionXAlignedInfiniteAnnulus.triggered.connect(self.XAlignedAnnulusDialog.exec)
        self.YAlignedAnnulusDialog = YAlignedAnnulusDialog()
        self.actionYAlignedInfiniteAnnulus.triggered.connect(self.YAlignedAnnulusDialog.exec)
        self.ZAlignedAnnulusDialog = ZAlignedAnnulusDialog()
        self.actionZAlignedInfiniteAnnulus.triggered.connect(self.ZAlignedAnnulusDialog.exec)

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
