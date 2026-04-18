import sys
import pandas as pd

from PyQt6.QtWidgets import QApplication

from MainWindow1 import MainWindow

from zapmenot.material import Material
from zapmenot.isotope import Isotope
from libraries import buildup_factor_materials, materials
import libraries
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

# use water as a dummy material to initialize the material class
# this prevents reloading the material databases for each
# dialog that requires it
dummy_material = Material('water')
# retrieve a list of materials that have buildup factors
for name in Material._library.keys():
    properties = Material._library.get(name)
    density = properties.get("density")
    materials[name] = density
    gp_data = properties.get("gp-coeff")
    if gp_data is not None:
        buildup_factor_materials.append(name)

dummy_isotope = Isotope('cs-137')
# create a pandas dataframe from the isotop dictionary
libraries.isotopes = pd.DataFrame.from_dict(Isotope._library, orient='index')
libraries.isotopes.drop(['half-life', 'half-life-units', 'key_progeny',
                         'photon-energy-units', 'photon-intensity'], axis=1,
                        inplace=True)
libraries.isotopes['active'] = False
libraries.isotopes['activity'] = '0.0'

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())
