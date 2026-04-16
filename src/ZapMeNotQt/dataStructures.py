import abc

# Each f the following classes are used to contain a set of data representing
# a feature in ZapMeNot.  Each class contains selected data as well as a method
# to summarize in a string all of the data in the class.


class Detector():
    def __init__(self, x, y, z):
        self.x_value = x
        self.y_value = y
        self.z_value = z

    def summarize(self):
        bodyText = "X: " + self.x_value + "\n"
        bodyText += "Y: " + self.y_value + "\n"
        bodyText += "Z: " + self.z_value + "\n"
        return bodyText

    def code(self):
        code_line = "detector = detector.Detector(x=" + self.x_value + \
            ", y=" + self.y_value + \
            ", z=" + self.z_value + ")"
        return code_line


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

    @abc.abstractmethod
    def code(self):
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

    def code(self):
        code = self.name + \
            "=shield.SemiInfiniteXSlab('" + self.material + "'" + \
            ", density=" + self.density + \
            ", x_start=" + self.radius1 + \
            ", x_end=" + self.radius2 + ")"
        return code


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

    # TODO: include the shell somehow
    def code(self):
        code = self.name + "=shield.Sphere('" + self.material + "'" + \
            ", density=" + self.density + \
            ", sphere_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", sphere_radius=" + self.radius1 + ")"
        if self.shell is not None:
            # append a discription of the shell
            shell_name = self.name + "_shell"
            code += "\n"
            code += shell_name + "=shield.Shell('" + \
                self.shell.material + "'" + \
                ", sphere=" + self.name + \
                ", density=" + self.shell.density + \
                ", thickness=" + self.shell.thickness + ")"
        return code


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

    def code(self):
        code = self.name + "=shield.Box('" + self.material + "'" + \
            ", density=" + self.density + \
            ", box_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", box_dimensions=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.InfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_origin=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_axis=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + \
            ", inner_radius=" + self.radius1 + \
            ", outer_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.XAlignedInfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", inner_radius=" + self.radius1 + \
            ", outer_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.YAlignedInfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", inner_radius=" + self.radius1 + \
            ", outer_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.ZAlignedInfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", inner_radius=" + self.radius1 + \
            ", outer_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = self.name + "=shield.CappedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_start=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_end=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + \
            ", cylinder_radius=" + self.radius1 + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.XAlignedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.YAlignedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = self.name + \
            "=shield.ZAlignedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code


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

    # TODO: include the shell somehow
    def code(self):
        code = "my_source" + "=source.SphereSource('" + self.material + "'" +\
            ", density=" + self.density + \
            ", sphere_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", sphere_radius=" + self.radius1 + ")"
        if self.shell is not None:
            # append a discription of the shell
            shell_name = "source_shell"
            code += "\n"
            code += shell_name + "=shield.Shell('" + \
                self.shell.material + "'" + \
                ", sphere=my_source" + \
                ", density=" + self.shell.density + \
                ", thickness=" + self.shell.thickness + ")"
        return code


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

    def code(self):
        code = "my_source" + "=source.BoxSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", box_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", box_dimensions=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + ")"
        return code


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

    def code(self):
        code = "my_source" + \
            "=source.XAlignedCylinderSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = "my_source" + \
            "=source.YAlignedCylinderSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = "my_source" + \
            "=source.ZAlignedCylinderSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code


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

    def code(self):
        code = "my_source" + "=source.PointSource(" + \
            "x=" + self.vector1[0] + \
            ", y=" + self.vector1[1] + \
            ", z=" + self.vector1[2] + ")"
        return code


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

    def code(self):
        code = "my_source" + "=source.LineSource(" + \
            ", start=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", end=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + ")"
        return code
