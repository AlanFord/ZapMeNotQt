import os

import PyQt6.QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QFile, QIODeviceBase
from PyQt6 import uic
from pathlib import Path
from DetectorLocationDialog import DetectorDialog
from OptionsGroupsDialog import OptionsGroupsDialog
from OptionsProgenyDialog import OptionsProgenyDialog
from OptionsQuadratureDialog import OptionsQuadratureDialog
from OptionsBuildupDialog import OptionsBuildupDialog
from OptionsFillerDialog import OptionsFillerDialog
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
from RemoveShieldDialog import RemoveShieldDialog
from SphereSourceDialog import SphereSourceDialog
from BoxSourceDialog import BoxSourceDialog
from XAlignedCylinderSourceDialog import XAlignedCylinderSourceDialog
from YAlignedCylinderSourceDialog import YAlignedCylinderSourceDialog
from ZAlignedCylinderSourceDialog import ZAlignedCylinderSourceDialog
from PointSourceDialog import PointSourceDialog
from LineSourceDialog import LineSourceDialog
from IsotopePickerDialog import IsotopePickerDialog
from PhotonDialog import PhotonDialog
from ScriptDisplayDialog import ScriptDisplayDialog

import libraries
import dataStructures


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

        # shield menu setup
        self.actionBox.triggered.connect(self.addBoxShieldSelected)
        self.actionSphere.triggered.connect(self.addSphereShieldSelected)
        self.actionSemiInfiniteXSlab.triggered.connect(
            self.addXSlabShieldSelected)
        self.actionInfiniteAnnulus.triggered.connect(
            self.addAnnulusShieldSelected)
        self.actionCappedCylinder.triggered.connect(
            self.addCappedCylinderShieldSelected)
        self.actionX_Aligned_Cylinder.triggered.connect(
            self.addXAlignedCylinderShieldSelected)
        self.actionY_Aligned_Cylinder.triggered.connect(
            self.addYAlignedCylinderShieldSelected)
        self.actionZ_Aligned_Cylinder.triggered.connect(
            self.addZAlignedCylinderShieldSelected)
        self.actionXAlignedInfiniteAnnulus.triggered.connect(
            self.addXAlignedAnnulusShieldSelected)
        self.actionYAlignedInfiniteAnnulus.triggered.connect(
            self.addYAlignedAnnulusShieldSelected)
        self.actionZAlignedInfiniteAnnulus.triggered.connect(
            self.addZAlignedAnnulusShieldSelected)
        self.actionRemove.triggered.connect(self.removeShieldSelected)

        # options menu setup
        self.actionEnergy_Groups.triggered.connect(self.energyGroupsSelected)
        self.actionDaughters.triggered.connect(self.progenySelected)
        self.actionBuildup_Material.triggered.connect(
            self.addBuildupFactorSelected)
        self.actionFiller_Material.triggered.connect(self.addFillerSelected)
        self.actionQuadrature_2.triggered.connect(self.quadratureSelected)

        # detector menu setup
        self.detectorDialog = DetectorDialog()
        self.location.triggered.connect(self.addDetectorSelected)

        # source menu setup
        self.actionSpherical_Source.triggered.connect(
            self.SphericalSourceSelected)
        self.actionBox_Source.triggered.connect(self.BoxSourceSelected)
        self.actionX_Aligned_Cylinder_Source.triggered.connect(
            self.XAlignedCylinderSourceSelected)
        self.actionY_Aligned_Cylinder_Source.triggered.connect(
            self.YAlignedCylinderSourceSelected)
        self.actionZ_Aligned_Cylinder_Source.triggered.connect(
            self.ZAlignedCylinderSourceSelected)
        self.actionPoint_Source.triggered.connect(self.PointSourceSelected)
        self.actionLine_Source.triggered.connect(self.LineSourceSelected)
        self.actionBy_Energy.triggered.connect(self.EnergySelected)
        self.actionBy_Isotope.triggered.connect(self.IsotopeSelected)
        self.actionImport.triggered.connect(self.notYetImplemented)

        # view menu setup
        self.actionGraphics.triggered.connect(self.notYetImplemented)
        self.actionPython_Script.triggered.connect(self.display_script)

        self.updateSummary()

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/MainWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()

    def display_script(self):
        script = self.format_script()
        show_me = ScriptDisplayDialog(script)
        show_me.exec()

    def format_script(self):
        script = []
        script.append("from zapmenot import model,source," +
                      "shield,detector,material")
        script.append("")
        script.append("my_model = model.Model()")
        script.append("")

        script.append("# Model Options")
        # filler material
        if libraries.filler_material != "None":
            code_line = "my_model.set_filler_material('" + \
                libraries.filler_material + "', density=" + \
                libraries.filler_density + ")"
            script.append(code_line)
        # buildup factor material
        if libraries.buildup_material == "None":
            QMessageBox.critical(self, "Error",
                                 " Buildup Factor Material has not " +
                                 "been specified.")
            script.append("# Missing buildup factor material!")
        else:
            code_line = "my_model.set_buildup_factor_material" + \
                "(material.Material('" + libraries.buildup_material + "'))"
            script.append(code_line)
        script.append("")

        script.append("# Detector")
        if libraries.detector is not None:
            script.append(libraries.detector.code())
        script.append("")

        script.append("# Shields")
        for shield in libraries.shield_dict.keys():
            script.append(libraries.shield_dict[shield].code())
            code_line = "my_model.add_shield(" + shield + ")"
            script.append(code_line)
            if isinstance(libraries.shield_dict[shield],
                          dataStructures.SphereShield):
                if libraries.shield_dict[shield].shell is not None:
                    code_line = "my_model.add_shield(" + shield + "_shell)"
                    script.append(code_line)
        script.append("")

        script.append("# Source Geometry")
        if libraries.source is not None:
            script.append(libraries.source.code())
        script.append("my_model.add_source(my_source)")
        if isinstance(libraries.source,
                        dataStructures.SphereSource):
            if libraries.source.shell is not None:
                code_line = "my_model.add_shield(source_shell)"
                script.append(code_line)
        script.append("")

        script.append("# Source Options")
        if libraries.progeny is True:
            code_line = "my_source.include_key_progeny = True"
        else:
            code_line = "my_source.include_key_progeny = False"
        script.append(code_line)
        # quadrature
        code_line = "my_source.points_per_dimension = [" + \
            str(libraries.quadrature[0]) + ", " + \
            str(libraries.quadrature[1]) + ", " + \
            str(libraries.quadrature[2]) + "]"
        script.append(code_line)
        # energy groups
        if libraries.groups == 0:
            code_line = 'my_source.grouping = "hybrid"'
        elif libraries.groups == 1:
            code_line = 'my_source.grouping = "group"'
        else:
            code_line = 'my_source.grouping = "discrete"'
        script.append(code_line)
        script.append("")

        script.append("# Source Isotopes")
        if libraries.activity_type == libraries.Activity_Type.Becquerel:
            code_line_start = "my_source.add_isotope_bq('"
        else:
            code_line_start = "my_source.add_isotope_curies('"
        data = libraries.isotopes.loc[libraries.isotopes['active']]
        if data.shape[0] != 0:
            # we have isotopes marked active
            for row in data.itertuples(index=True):
                # TODO: why is activity stored as a float?
                code_line = code_line_start + row.Index + "', " + \
                    str(row.activity) + ")"
                script.append(code_line)
        script.append("")

        # TODO: look into why these values are stored as floats and not strings
        script.append("# Source Discrete Photon Energies")
        for photon in libraries.photons:
            energy = photon[0]
            intensity = photon[1]
            if energy != "" and intensity != "":
                code_line = "my_source.add_photon(" + str(energy) + \
                    ", " + str(intensity) + ")"
                script.append(code_line)
        script.append("")

        return script

    def EnergySelected(self):
        if PhotonDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def IsotopeSelected(self):
        if IsotopePickerDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def removeShieldSelected(self):
        if RemoveShieldDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def progenySelected(self):
        if OptionsProgenyDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def energyGroupsSelected(self):
        if OptionsGroupsDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def quadratureSelected(self):
        if OptionsQuadratureDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addBuildupFactorSelected(self):
        if OptionsBuildupDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addFillerSelected(self):
        if OptionsFillerDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addDetectorSelected(self):
        if DetectorDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

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

    def SphericalSourceSelected(self):
        if SphereSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def BoxSourceSelected(self):
        if BoxSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def PointSourceSelected(self):
        if PointSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def LineSourceSelected(self):
        if LineSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def XAlignedCylinderSourceSelected(self):
        if XAlignedCylinderSourceDialog().exec() == \
                QDialog.DialogCode.Accepted:
            self.updateSummary()

    def YAlignedCylinderSourceSelected(self):
        if YAlignedCylinderSourceDialog().exec() == \
                QDialog.DialogCode.Accepted:
            self.updateSummary()

    def ZAlignedCylinderSourceSelected(self):
        if ZAlignedCylinderSourceDialog().exec() == \
                QDialog.DialogCode.Accepted:
            self.updateSummary()

    def notYetImplemented(self):
        QMessageBox.information(self, "Sadly,",
                                "This feature is not yet implemented.")

    def updateSummary(self):
        bodyText = "Model Summary: \n\n"

        bodyText += "Buildup Factor Material:  " + \
                    libraries.buildup_material + "\n\n"

        bodyText += "Filler Material:  " + \
                    libraries.filler_material + ", " + \
                    libraries.filler_density + " g/cm3\n\n"

        bodyText += "Include Selected Progeny in Equilibrium:  "
        if libraries.progeny is True:
            bodyText += "Yes\n\n"
        else:
            bodyText += "No\n\n"

        bodyText += "Energy Group Option:  "
        if libraries.groups == 0:
            bodyText += "Standard Hybrid Set\n\n"
        elif libraries.groups == 1:
            bodyText += "30 Linear Energy Groups\n\n"
        else:
            bodyText += "Discrete Photon Energies\n\n"

        bodyText += "Source Quadrature: " + \
            str(libraries.quadrature[0]) + ", " +\
            str(libraries.quadrature[1]) + ", " +\
            str(libraries.quadrature[2]) +\
            "\n\n"

        bodyText += "***Detector*** \n"
        if libraries.detector is not None:
            bodyText += libraries.detector.summarize() + "\n"
        else:
            bodyText += "Not Yet Specified\n\n"

        bodyText += "***Shields*** \n"
        keys = libraries.shield_dict.keys()
        if not keys:
            bodyText += "None Specified\n\n"
            self.actionRemove.setEnabled(False)
        else:
            self.actionRemove.setEnabled(True)
            for key in keys:
                bodyText += libraries.shield_dict[key].summarize() + "\n"

        bodyText += "***Source Geometry*** \n"
        if libraries.source is not None:
            bodyText += libraries.source.summarize() + "\n"
        else:
            bodyText += "Not Yet Specified\n\n"

        bodyText += "***Source Isotopes*** \n"
        if libraries.activity_type == libraries.Activity_Type.Becquerel:
            units = "Bq"
        else:
            units = "Ci"
        data = libraries.isotopes.loc[libraries.isotopes['active']]
        if data.shape[0] > 0:
            for index in data.index:
                bodyText += index + ": " + \
                    data.loc[index, 'activity'].astype(str) + " " + units + \
                    "\n"
            bodyText += "\n"
        else:
            bodyText += "None Specified\n\n"

        bodyText += "***Discrete Source Photons*** \n"
        data = libraries.photons
        count = 0
        for row in data:
            if row[0] != "" and row[1] != "":
                count += 1
                energy = row[0]
                intensity = row[1]
                bodyText += str(energy) + " MeV: " + \
                    str(intensity) + " " + "photons/sec" + \
                    "\n"
        if count == 0:
            bodyText += "None Specified\n"
        bodyText += "\n"

        self.summaryDescription.setText(bodyText)
