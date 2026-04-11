import abc

# Each f the following classes are used to contain a set of data representing
# a feature in ZapMeNot.  Each class contains selected data as well as a method
# to summarize in a string all of the data in the class.

class LocationData():
    def __init__(self, x, y, z):
        self.x_value = x
        self.y_value = y
        self.z_value = z

    def summarize(self):
        bodyText = "X: " + self.x_value + "\n"
        bodyText += "Y: " + self.y_value + "\n"
        bodyText += "Z: " + self.z_value + "\n"
        return bodyText


class ShieldData(abc.ABC):
    def __init__(self):
        super().__init__()
        self.description = ""
        self.name = ""
        self.material = ""
        self.density = ""
        self.vector1 = ["", "", ""]
        self.vector2 = ["", "", ""]
        self.radius1 = ""
        self.radius2 = ""
        self.shell = None

    @abc.abstractmethod
    def summarize(self):
        pass


class XSlabShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Infinite X Slab"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "X-start: " + self.radius1 + "\n"
        bodyText += "X-end: " + self.radius2 + "\n"
        return bodyText


class SphereShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Sphere"
        self.shell = None

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Location: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Radius: " + self.radius1 + "\n"
        if self.shell is not None:
            bodyText += "Shell: \n"
            bodyText += self.shell.summarize()
        else:
            bodyText += "Shell: None \n"
        return bodyText


class ShellShield():
    def __init__(self):
        self.material = None
        self.density = None
        self.thickness = None

    def summarize(self):
        bodyText = "    Material: " + self.material + "\n"
        bodyText += "    Density: " + self.density + "\n"
        bodyText += "    Thickness: " + self.thickness + "\n"
        return bodyText


class BoxShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Box"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Box Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Dimensions: " + \
            self.vector2[0] + " " + \
            self.vector2[1] + " " + \
            self.vector2[2] + "\n"
        return bodyText


class AnnulusShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Infinite Annulus"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Location: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Axis: " + \
            self.vector2[0] + " " + \
            self.vector2[1] + " " + \
            self.vector2[2] + "\n"
        bodyText += "Inner Radius: " + self.radius1 + "\n"
        bodyText += "Outer Radius: " + self.radius2 + "\n"
        return bodyText


class XAnnulusShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "X-Aligned Infinite Annulus"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Annulus Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Inner Radius: " + self.radius1 + "\n"
        bodyText += "Outer Radius: " + self.radius2 + "\n"
        return bodyText


class YAnnulusShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Y-Aligned Infinite Annulus"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Annulus Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Inner Radius: " + self.radius1 + "\n"
        bodyText += "Outer Radius: " + self.radius2 + "\n"
        return bodyText


class ZAnnulusShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Z-Aligned Infinite Annulus"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Annulus Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Inner Radius: " + self.radius1 + "\n"
        bodyText += "Outer Radius: " + self.radius2 + "\n"
        return bodyText


class CappedCylinderShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Capped Cylinder"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Start: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Cylinder End: " + \
            self.vector2[0] + " " + \
            self.vector2[1] + " " + \
            self.vector2[2] + "\n"
        bodyText += "Radius: " + self.radius1 + "\n"
        return bodyText


class XCylinderShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "X-Aligned Cylinder"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Length: " + self.radius1 + "\n"
        bodyText += "Radius: " + self.radius2 + "\n"
        return bodyText


class YCylinderShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Y-Aligned Cylinder"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Length: " + self.radius1 + "\n"
        bodyText += "Radius: " + self.radius2 + "\n"
        return bodyText


class ZCylinderShield(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Z-Aligned Cylinder"

    def summarize(self):
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Length: " + self.radius1 + "\n"
        bodyText += "Radius: " + self.radius2 + "\n"
        return bodyText


class SphereSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Sphere"
        self.shell = None

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Location: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Radius: " + self.radius1 + "\n"
        if self.shell is not None:
            bodyText += "Shell: \n"
            bodyText += self.shell.summarize()
        else:
            bodyText += "Shell: None \n"
        return bodyText


class BoxSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Box"

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Box Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Dimensions: " + \
            self.vector2[0] + " " + \
            self.vector2[1] + " " + \
            self.vector2[2] + "\n"
        return bodyText


class XCylinderSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "X-Aligned Cylinder"

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Length: " + self.radius1 + "\n"
        bodyText += "Radius: " + self.radius2 + "\n"
        return bodyText


class YCylinderSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Y-Aligned Cylinder"

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Length: " + self.radius1 + "\n"
        bodyText += "Radius: " + self.radius2 + "\n"
        return bodyText


class ZCylinderSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Z-Aligned Cylinder"

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + "\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Length: " + self.radius1 + "\n"
        bodyText += "Radius: " + self.radius2 + "\n"
        return bodyText


class PointSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Point"

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Location: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        return bodyText


class LineSource(ShieldData):
    def __init__(self):
        super().__init__()
        self.description = "Line"

    def summarize(self):
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Starting Location: " + \
            self.vector1[0] + " " + \
            self.vector1[1] + " " + \
            self.vector1[2] + "\n"
        bodyText += "Ending Location: " + \
            self.vector2[0] + " " + \
            self.vector2[1] + " " + \
            self.vector2[2] + "\n"
        return bodyText
