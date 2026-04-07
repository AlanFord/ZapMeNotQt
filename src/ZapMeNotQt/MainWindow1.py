import os

import PyQt6.QtWidgets
from PyQt6.QtWidgets import QDialog
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

import libraries


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

        # shield menu setup
        self.actionBox.triggered.connect(self.addBoxShieldSelected)
        self.actionSphere.triggered.connect(self.addSphereShieldSelected)
        self.actionSemiInfiniteXSlab.triggered.connect(self.addXSlabShieldSelected)
        self.actionInfiniteAnnulus.triggered.connect(self.addAnnulusShieldSelected)
        self.actionCappedCylinder.triggered.connect(self.addCappedCylinderShieldSelected)
        self.actionX_Aligned_Cylinder.triggered.connect(self.addXAlignedCylinderShieldSelected)
        self.actionY_Aligned_Cylinder.triggered.connect(self.addYAlignedCylinderShieldSelected)
        self.actionZ_Aligned_Cylinder.triggered.connect(self.addZAlignedCylinderShieldSelected)
        self.actionXAlignedInfiniteAnnulus.triggered.connect(self.addXAlignedAnnulusShieldSelected)
        self.actionYAlignedInfiniteAnnulus.triggered.connect(self.addYAlignedAnnulusShieldSelected)
        self.actionZAlignedInfiniteAnnulus.triggered.connect(self.addZAlignedAnnulusShieldSelected)

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

    def addBoxShieldSelected(self):
        if BoxDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addSphereShieldSelected(self):
        if SphereDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addXSlabShieldSelected(self):
        if XSlabDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addAnnulusShieldSelected(self):
        if AnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addCappedCylinderShieldSelected(self):
        if CappedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addXAlignedCylinderShieldSelected(self):
        if XAlignedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addYAlignedCylinderShieldSelected(self):
        if YAlignedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addZAlignedCylinderShieldSelected(self):
        if ZAlignedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addXAlignedAnnulusShieldSelected(self):
        if XAlignedAnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addYAlignedAnnulusShieldSelected(self):
        if YAlignedAnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addZAlignedAnnulusShieldSelected(self):
        if ZAlignedAnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def updateSummary(self):
        bodyText = "Model Summary: \n\n"

        bodyText += "***Shields*** \n"
        for key in libraries.shield_dict.keys():
            bodyText = bodyText + libraries.shield_dict[key].summarize() + "\n"
        self.summaryDescription.setText(bodyText)
