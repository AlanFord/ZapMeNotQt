# here we create a set of global libraries used by several of the dialogs
# and windows.  Each module should import libraries.py

import pandas as pd
from enum import Enum


class Activity_Type(Enum):
    Curie = 1
    Becquerel = 2


# holds the user specified activity units
activity_type = Activity_Type.Curie

# list of available materials that can be used for a buildup factor
buildup_factor_materials: list[str] = []

# dictionary of material densities
materials: dict = {}

# dictionary of source isotopes, each entry being a list of 1)
# included (True,False) and concentration (float)
isotopes = pd.DataFrame()
# 2-d list of lists containing photon source energies and intensities
photons = []

# these data are used to track user input and are populated by
# a number of dialogs
shield_dict: dict = {}
source = None
detector = None
quadrature = [10, 10, 10]
buildup_material = "None"
filler_material = "None"
progeny = False
# 0=standard hybrid
# 1=30 groups
# 2=discrete
groups = 0
