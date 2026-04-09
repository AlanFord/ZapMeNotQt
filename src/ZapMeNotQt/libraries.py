# here we create a set of global libraries used by several of the dialogs
# and windows.  Each module should import libraries.py
buildup_factor_materials: list[str] = []
materials = {}
isotopes: list[str] = []

# these data are used to track user input
shield_dict = {}
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
