import pandas as pd
import pickle
import os
import io

import PyQt6.QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog

from DescriptionDialog import DescriptionDialog
from OutputDisplayDialog import OutputDisplayDialog
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
from GraphicsDisplayDialog import GraphicsDisplayDialog
import libraries
from libraries import buildup_factor_materials, materials
import dataStructures

from ui.MainWindow import Ui_MainWindow

from zapmenot.material import Material
from zapmenot.isotope import Isotope

''' '''
'''
ZapMeNotQt - a graphical user interface for ZapMeNot
Copyright (C) 2026  C. Alan Ford

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


class MainWindow(PyQt6.QtWidgets.QMainWindow, Ui_MainWindow):
    def runSelected(self) -> None:
        # verify that the model has sufficient detail to run
        # - a source
        # - a detector
        # - if there is any form of shield(even a source/shield)
        #   or filler material, a buildup factor.  This might
        #   just be a caution
        problem_to_run = self.format_script(silent=True)
        multiline_string = "\n".join(problem_to_run)
        these_globals = {}
        these_locals = {}
        exec(multiline_string, these_globals, these_locals)
        # TODO: trap errors from an exec() run to display in a dialog
                    # script.append("summary = my_model.generate_summary()")
        column_names = pd.DataFrame([["", "Photons", "Energy", "MeV"],
                                        ["", "Photons", "Intensity", "photons/sec"],
                                        ["", "Uncollided", "Energy Flux", "MeV/cm2/sec"],
                                        ["", "Uncollided", "Exposure", "mR/hr"],
                                        ["Collided+", "Uncollided", "Exposure", "mR/hr"]],
                                        columns=["", "", "", ""])
        columns = pd.MultiIndex.from_frame(column_names)
        summary = these_locals['summary']
        result = these_locals['result']
        df = pd.DataFrame(summary, columns=columns)
        uncollided_total = df.iloc[:, 3].sum()

        buffer = io.StringIO()        
        # output header
        if libraries.model.description != "":
            print(libraries.model.description, file=buffer)

        # add model summary to output
        print(self.summaryDescription.toPlainText(), file=buffer)

        # add results to output
        print("  ", file=buffer)
        print("  ", file=buffer)
        print("\n\nResults:", file=buffer)
        print("Total Exposure is ", result, " mR/hr", file=buffer)
        print("Total Uncollided Exposure is ", uncollided_total, " mR/hr", file=buffer)
        print(df.to_string(index=False), file=buffer)
        
        show_me = OutputDisplayDialog(buffer.getvalue())
        show_me.exec()


    def openFileSelected(self) -> None:
        # Open the save file dialog
        filename, _ = QFileDialog.getOpenFileName(None,
                                                  "Save File",
                                                  "",
                                                  "ZapMeNot Files (*.zp);;All Files (*)")
        if filename:
            # TODO: trap errors if invalid file is opened
            with open(filename, 'rb') as file:
                libraries.model = pickle.load(file)
            self.file_name = filename
            self.setWindowTitle("ZapMeNotQt - " + os.path.basename(self.file_name))
            self.actionSave.setEnabled(True)
            self.updateSummary()

    def saveFileSelected(self) -> None:
            # Proceed to save the file using the existing filename, if there is one
            if self.file_name != "":
                with open(self.file_name, 'wb') as file:
                    pickle.dump(libraries.model, file)
                file.close()
            else:
                self.saveAsSelected()

    def saveAsSelected(self) -> None:
        # Open the save file dialog
        filename, _ = QFileDialog.getSaveFileName(None,
                                                  "Save File",
                                                  "",
                                                  "ZapMeNot Files (*.zp);;All Files (*)")
        if filename:
            # Proceed to save the file using the selected filename
            with open(filename, 'wb') as file:
                pickle.dump(libraries.model, file)
                self.file_name = filename
            file.close()
            self.actionSave.setEnabled(True)
            self.file_name = filename
            self.setWindowTitle("ZapMeNotQt - " + os.path.basename(self.file_name))

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.file_name = ""
        self.setWindowTitle("ZapMeNotQt - Not Saved")

        # file menu setup
        self.actionOpen.triggered.connect(self.openFileSelected)
        self.actionSave.triggered.connect(self.saveFileSelected)
        self.actionSave_As.triggered.connect(self.saveAsSelected)
        self.actionSave.setEnabled(False)
        self.actionRun.triggered.connect(self.runSelected)

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
        self.actionCase_Description.triggered.connect(self.descriptionSelected)
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
        self.actionGraphics.triggered.connect(self.display_graphics)
        self.actionPython_Script.triggered.connect(self.display_script)

        # use water as a dummy material to initialize the material class
        # this prevents reloading the material databases for each
        # dialog that requires it
        Material('water')
        # retrieve a list of materials that have buildup factors
        for name in Material._library.keys():
            properties = Material._library.get(name)
            if properties is not None:
                density = properties.get("density")
                materials[name] = density
                gp_data = properties.get("gp-coeff")
                if gp_data is not None:
                    buildup_factor_materials.append(name)
                else:
                    # TODO: throw an error
                    pass
            else:
                # TODO: throw an error
                pass

        # use a dummy isotope to initialize the isotope class
        Isotope('cs-137')
        if not Isotope._library:
            # TODO: throw an error because the library didn't load
            pass
        # create a pandas dataframe from the isotope dictionary
        libraries.model.isotopes = pd.DataFrame.from_dict(Isotope._library, orient='index')
        libraries.model.isotopes.drop(['half-life', 'half-life-units', 'key_progeny',
                                'photon-energy-units', 'photon-intensity'], axis=1,
                                inplace=True)
        libraries.model.isotopes['active'] = False
        libraries.model.isotopes['activity'] = '0.0'

        self.updateSummary()

    def display_script(self) -> None:
        script: list[str] = self.format_script(silent=False)
        show_me = ScriptDisplayDialog(script)
        show_me.exec()

    def descriptionSelected(self) -> None:
        if DescriptionDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def display_graphics(self) -> None:
        # do we have sufficient model detail to display?
        if libraries.model.source is None or libraries.model.detector is None:
            QMessageBox.critical(self, "Error",
                                 "Please specify both a source and \
                                    detector before displaying the model.")
        else:
            show_me = GraphicsDisplayDialog(" ")
            show_me.exec()

    def format_script(self, silent: bool) -> list[str]:
        script: list[str] = []
        script.append("from zapmenot import model,source," +
                      "shield,detector,material")
        script.append("")
        script.append("# Description: " + libraries.model.description)
        script.append("")
        script.append("my_model = model.Model()")
        script.append("")

        script.append("# Model Options")
        # filler material
        if libraries.model.filler_material != "None":
            code_line = "my_model.set_filler_material('" + \
                libraries.model.filler_material + "', density=" + \
                libraries.model.filler_density + ")"
            script.append(code_line)
        # buildup factor material
        if libraries.model.buildup_material == "None":
            # TODO: move this to a "check input" function that can be use when displaying script or running case
            pass
            # QMessageBox.critical(self, "Error",
            #                      " Buildup Factor Material has not " +
            #                      "been specified.")
            # script.append("# Missing buildup factor material!")
        else:
            code_line = "my_model.set_buildup_factor_material" + \
                "(material.Material('" + libraries.model.buildup_material + "'))"
            script.append(code_line)
        script.append("")

        script.append("# Detector")
        if libraries.model.detector is not None:
            script.append(libraries.model.detector.script())
            script.append("my_model.add_detector(my_detector)")
        script.append("")

        script.append("# Shields")
        for shield in libraries.model.shield_dict.keys():
            script.append(libraries.model.shield_dict[shield].script())
            code_line = "my_model.add_shield(" + shield + ")"
            script.append(code_line)
            if isinstance(libraries.model.shield_dict[shield],
                          dataStructures.SphereShield):
                if libraries.model.shield_dict[shield].shell is not None:
                    code_line = "my_model.add_shield(" + shield + "_shell)"
                    script.append(code_line)
        script.append("")

        script.append("# Source Geometry")
        if libraries.model.source is not None:
            script.append(libraries.model.source.script())
            script.append("my_model.add_source(my_source)")
            if isinstance(libraries.model.source,
                          dataStructures.SphereSource):
                if libraries.model.source.shell is not None:
                    code_line = "my_model.add_shield(source_shell)"
                    script.append(code_line)
        script.append("")

        script.append("# Source Options")
        if libraries.model.progeny is True:
            code_line = "my_source.include_key_progeny = True"
        else:
            code_line = "my_source.include_key_progeny = False"
        script.append(code_line)
        # quadrature
        code_line = "my_source.points_per_dimension = [" + \
            libraries.model.quadrature[0] + ", " + \
            libraries.model.quadrature[1] + ", " + \
            libraries.model.quadrature[2] + "]"
        script.append(code_line)
        # energy groups
        if libraries.model.groups == 0:
            code_line = 'my_source.grouping = "hybrid"'
        elif libraries.model.groups == 1:
            code_line = 'my_source.grouping = "group"'
        else:
            code_line = 'my_source.grouping = "discrete"'
        script.append(code_line)
        script.append("")

        script.append("# Source Isotopes")
        if libraries.model.activity_type == dataStructures.Activity_Type.Becquerel:
            code_line_start = "my_source.add_isotope_bq('"
        else:
            code_line_start = "my_source.add_isotope_curies('"
        data = libraries.model.isotopes.loc[libraries.model.isotopes['active']]
        if data.shape[0] != 0:
            # we have isotopes marked active
            for row in data.itertuples(index=True):
                code_line = code_line_start + str(row.Index) + "', " + \
                    str(row.activity) + ")"
                script.append(code_line)
        script.append("")

        script.append("# Source Discrete Photon Energies")
        for photon in libraries.model.photons:
            energy = photon[0]
            intensity = photon[1]
            if energy != "" and intensity != "":
                code_line = "my_source.add_photon(" + energy + \
                    ", " + intensity + ")"
                script.append(code_line)
        script.append("")
        script.append("result = my_model.calculate_exposure()")
        if not silent:
            script.append('print("The exposure rate is ", result, " mR/hr")')
        else:
            script.append("summary = my_model.generate_summary()")
        return script

    def EnergySelected(self) -> None:
        if PhotonDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def IsotopeSelected(self) -> None:
        if IsotopePickerDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def removeShieldSelected(self) -> None:
        if RemoveShieldDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def progenySelected(self) -> None:
        if OptionsProgenyDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def energyGroupsSelected(self) -> None:
        if OptionsGroupsDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def quadratureSelected(self) -> None:
        if OptionsQuadratureDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addBuildupFactorSelected(self) -> None:
        if OptionsBuildupDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addFillerSelected(self) -> None:
        if OptionsFillerDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addDetectorSelected(self) -> None:
        if DetectorDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addBoxShieldSelected(self) -> None:
        if BoxDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addSphereShieldSelected(self) -> None:
        if SphereDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addXSlabShieldSelected(self) -> None:
        if XSlabDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addAnnulusShieldSelected(self) -> None:
        if AnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addCappedCylinderShieldSelected(self) -> None:
        if CappedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addXAlignedCylinderShieldSelected(self) -> None:
        if XAlignedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addYAlignedCylinderShieldSelected(self) -> None:
        if YAlignedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addZAlignedCylinderShieldSelected(self) -> None:
        if ZAlignedCylinderDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addXAlignedAnnulusShieldSelected(self) -> None:
        if XAlignedAnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addYAlignedAnnulusShieldSelected(self) -> None:
        if YAlignedAnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def addZAlignedAnnulusShieldSelected(self) -> None:
        if ZAlignedAnnulusDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def SphericalSourceSelected(self) -> None:
        if SphereSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def BoxSourceSelected(self) -> None:
        if BoxSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def PointSourceSelected(self) -> None:
        if PointSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def LineSourceSelected(self) -> None:
        if LineSourceDialog().exec() == QDialog.DialogCode.Accepted:
            self.updateSummary()

    def XAlignedCylinderSourceSelected(self) -> None:
        if XAlignedCylinderSourceDialog().exec() == \
                QDialog.DialogCode.Accepted:
            self.updateSummary()

    def YAlignedCylinderSourceSelected(self) -> None:
        if YAlignedCylinderSourceDialog().exec() == \
                QDialog.DialogCode.Accepted:
            self.updateSummary()

    def ZAlignedCylinderSourceSelected(self) -> None:
        if ZAlignedCylinderSourceDialog().exec() == \
                QDialog.DialogCode.Accepted:
            self.updateSummary()

    def notYetImplemented(self) -> None:
        QMessageBox.information(self, "Sadly,",
                                "This feature is not yet implemented.")

    def updateSummary(self) -> None:
        bodyText = "Model Summary: \n\n"

        bodyText += "Description: " + \
                    libraries.model.description + "\n\n"

        bodyText += "Buildup Factor Material:  " + \
                    libraries.model.buildup_material + "\n\n"

        bodyText += "Filler Material:  " + \
                    libraries.model.filler_material + ", " + \
                    libraries.model.filler_density + " g/cm3\n\n"

        bodyText += "Include Selected Progeny in Equilibrium:  "
        if libraries.model.progeny is True:
            bodyText += "Yes\n\n"
        else:
            bodyText += "No\n\n"

        bodyText += "Energy Group Option:  "
        if libraries.model.groups == 0:
            bodyText += "Standard Hybrid Set\n\n"
        elif libraries.model.groups == 1:
            bodyText += "30 Linear Energy Groups\n\n"
        else:
            bodyText += "Discrete Photon Energies\n\n"

        bodyText += "Source Quadrature: " + \
            str(libraries.model.quadrature[0]) + ", " +\
            str(libraries.model.quadrature[1]) + ", " +\
            str(libraries.model.quadrature[2]) +\
            "\n\n"

        bodyText += "***Detector Location*** \n"
        if libraries.model.detector is not None:
            bodyText += libraries.model.detector.summarize() + "\n"
        else:
            bodyText += "Not Yet Specified\n\n"

        bodyText += "***Shields*** \n"
        keys = libraries.model.shield_dict.keys()
        if not keys:
            bodyText += "None Specified\n\n"
            self.actionRemove.setEnabled(False)
        else:
            self.actionRemove.setEnabled(True)
            for key in keys:
                bodyText += libraries.model.shield_dict[key].summarize() + "\n"

        bodyText += "***Source Geometry*** \n"
        if libraries.model.source is not None:
            bodyText += libraries.model.source.summarize() + "\n"
        else:
            bodyText += "Not Yet Specified\n\n"

        bodyText += "***Source Isotopes*** \n"
        if libraries.model.activity_type == dataStructures.Activity_Type.Becquerel:
            units = "Bq"
        else:
            units = "Ci"
        data = libraries.model.isotopes.loc[libraries.model.isotopes['active']]
        if data.shape[0] > 0:
            for index in data.index:
                bodyText += index + ": " + \
                    data.loc[index, 'activity'] + " " + units + \
                    "\n"
            bodyText += "\n"
        else:
            bodyText += "None Specified\n\n"

        bodyText += "***Discrete Source Photons*** \n"
        data = libraries.model.photons
        count = 0
        for row in data:
            if row[0] != "" and row[1] != "":
                count += 1
                energy = row[0]
                intensity = row[1]
                bodyText += energy + " MeV: " + \
                    intensity + " " + "photons/sec" + \
                    "\n"
        if count == 0:
            bodyText += "None Specified\n"
        bodyText += "\n"

        self.summaryDescription.setPlainText(bodyText)
