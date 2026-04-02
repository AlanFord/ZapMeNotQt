# here we create a set of global libraries used by several of the dialogs
# and windows.  Each module should import libraries.py
buildup_factor_materials: list[str] = []
materials = {}
isotopes: list[str] = []

shield_dict = {}
source = None
detector = None
