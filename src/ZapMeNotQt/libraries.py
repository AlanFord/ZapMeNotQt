# here we create a set of global libraries used by several of the dialogs
# and windows.  Each module should import libraries.py

# from typing import Optional
# import pandas as pd
#from enum import Enum
# from dataStructures import ShieldData, Detector
from dataStructures import Model
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


model = Model()

# class Activity_Type(Enum):
#     Curie = 1
#     Becquerel = 2


# # holds the user specified activity units
# activity_type = Activity_Type.Curie

# list of available materials that can be used for a buildup factor
buildup_factor_materials: list[str] = []

# dictionary of material densities
materials: dict[str, float] = {}

# # dictionary of source isotopes, each entry being a list of 1)
# # included (True,False) and concentration (str)
# isotopes = pd.DataFrame()
# # 2-d list of lists containing photon source energies and intensities
# photons: list[list[str]] = []

# # these data are used to track user input and are populated by
# # a number of dialogs
# shield_dict: dict[str, ShieldData] = {}
# source: Optional[ShieldData] = None
# detector: Optional[Detector] = None
# quadrature: list[float] = [10, 10, 10]
# buildup_material: str = "None"
# filler_material: str = "None"
# filler_density: str = "0.0"
# progeny: bool = False
# # 0=standard hybrid
# # 1=30 groups
# # 2=discrete
# groups: int = 0
