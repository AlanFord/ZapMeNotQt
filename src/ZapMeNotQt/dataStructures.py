import abc
from typing import Optional
from zapmenot import model, source, shield, detector, material
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

# Each of the following classes are used to contain a set of data representing
# a feature in ZapMeNot.  Each class contains selected data as well as a method
# to summarize in a string all of the data in the class.


class Detector:
    def __init__(self, x: str, y: str, z: str) -> None:
        self.x_value: str = x
        self.y_value: str = y
        self.z_value: str = z

    def summarize(self) -> str:
        bodyText = "X: " + self.x_value + " cm\n"
        bodyText += "Y: " + self.y_value + " cm\n"
        bodyText += "Z: " + self.z_value + " cm\n"
        return bodyText

    def code(self) -> str:
        code_line = "detector = detector.Detector(x=" + self.x_value + \
            ", y=" + self.y_value + \
            ", z=" + self.z_value + ")"
        return code_line

    def phalax(self) -> detector.Detector:
        local_detector = detector.Detector(x=float(self.x_value),
                                           y=float(self.y_value),
                                           z=float(self.z_value))
        return local_detector


class ShieldData(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.description: str = ""
        self.name: str = ""
        self.material: str = ""
        self.density: str = ""
        self.vector1: list[str] = ["", "", ""]
        self.vector2: list[str] = ["", "", ""]
        self.radius1: str = ""
        self.radius2: str = ""
        self.shell: Optional['ShellShield'] = None

    @abc.abstractmethod
    def summarize(self) -> str:
        pass

    @abc.abstractmethod
    def code(self) -> str:
        pass

    @abc.abstractmethod
    def phalax(self) -> list[shield.Shield]:
        pass


class XSlabShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Infinite X Slab"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "X-start: " + self.radius1 + "cm\n"
        bodyText += "X-end: " + self.radius2 + "cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.SemiInfiniteXSlab('" + self.material + "'" + \
            ", density=" + self.density + \
            ", x_start=" + self.radius1 + \
            ", x_end=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.SemiInfiniteXSlab(self.material,
                                     density=float(self.density),
                                     x_start=float(self.radius1),
                                     x_end=float(self.radius2))
        return [local_shield]


class SphereShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Sphere"
        self.shell: Optional['ShellShield'] = None

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Location: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Radius: " + self.radius1 + " cm\n"
        if self.shell is not None:
            bodyText += "Shell: \n"
            bodyText += self.shell.summarize()
        else:
            bodyText += "Shell: None \n"
        return bodyText

    def code(self) -> str:
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

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.Sphere(self.material,
                          density=float(self.density),
                          sphere_center=[float(self.vector1[0]),
                                         float(self.vector1[1]),
                                         float(self.vector1[2])],
                          sphere_radius=float(self.radius1))
        if self.shell is not None:
            local_shell = \
                shield.Shell(self.shell.material,
                             sphere=local_shield,
                             density=float(self.shell.density),
                             thickness=float(self.shell.thickness))
            return [local_shield, local_shell]
        return [local_shield]


class ShellShield:
    def __init__(self) -> None:
        self.material: Optional[str] = None
        self.density: Optional[str] = None
        self.thickness: Optional[str] = None

    def summarize(self) -> str:
        bodyText = "    Material: " + self.material + "\n"
        bodyText += "    Density: " + self.density + " g/cm3\n"
        bodyText += "    Thickness: " + self.thickness + " cm\n"
        return bodyText


class BoxShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Box"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Box Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Dimensions: " + \
            self.vector2[0] + " cm, " + \
            self.vector2[1] + " cm, " + \
            self.vector2[2] + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + "=shield.Box('" + self.material + "'" + \
            ", density=" + self.density + \
            ", box_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", box_dimensions=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.Box(self.material,
                       density=float(self.density),
                       box_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                       box_dimensions=[float(self.vector1[0]),
                                       float(self.vector1[1]),
                                       float(self.vector1[2])])
        return [local_shield]


class AnnulusShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Infinite Annulus"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Location: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Axis: " + \
            self.vector2[0] + " cm, " + \
            self.vector2[1] + " cm, " + \
            self.vector2[2] + " cm\n"
        bodyText += "Inner Radius: " + self.radius1 + " cm\n"
        bodyText += "Outer Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.InfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_origin=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_axis=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + \
            ", cylinder_inner_radius=" + self.radius1 + \
            ", cylinder_outer_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.InfiniteAnnulus(self.material,
                       density=float(self.density),
                       cylinder_origin=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                       cylinder_axis=[float(self.vector1[0]),
                                       float(self.vector1[1]),
                                       float(self.vector1[2])],
                        cylinder_inner_radius=float(self.radius1),
                        cylinder_outer_radius=float(self.radius2))
        return [local_shield]


class XAnnulusShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "X-Aligned Infinite Annulus"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Annulus Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Inner Radius: " + self.radius1 + " cm\n"
        bodyText += "Outer Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.XAlignedInfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_inner_radius=" + self.radius1 + \
            ", cylinder_outer_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.XAlignedInfiniteAnnulus(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_inner_radius=float(self.radius1),
                        cylinder_outer_radius=float(self.radius2))
        return [local_shield]


class YAnnulusShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Y-Aligned Infinite Annulus"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Annulus Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Inner Radius: " + self.radius1 + " cm\n"
        bodyText += "Outer Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.YAlignedInfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", inner_radius=" + self.radius1 + \
            ", outer_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.YAlignedInfiniteAnnulus(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_inner_radius=float(self.radius1),
                        cylinder_outer_radius=float(self.radius2))
        return [local_shield]


class ZAnnulusShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Z-Aligned Infinite Annulus"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Annulus Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Inner Radius: " + self.radius1 + " cm\n"
        bodyText += "Outer Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.ZAlignedInfiniteAnnulus('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", inner_radius=" + self.radius1 + \
            ", outer_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.ZAlignedInfiniteAnnulus(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_inner_radius=float(self.radius1),
                        cylinder_outer_radius=float(self.radius2))
        return [local_shield]


class CappedCylinderShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Capped Cylinder"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Start: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Cylinder End: " + \
            self.vector2[0] + " cm, " + \
            self.vector2[1] + " cm, " + \
            self.vector2[2] + " cm\n"
        bodyText += "Radius: " + self.radius1 + " cm\n"
        return bodyText

    def code(self) -> str:
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

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.CappedCylinder(self.material,
                       density=float(self.density),
                       cylinder_start=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                       cylinder_end=[float(self.vector1[0]),
                                       float(self.vector1[1]),
                                       float(self.vector1[2])],
                        cylinder_radius=float(self.radius1))
        return [local_shield]


class XCylinderShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "X-Aligned Cylinder"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Length: " + self.radius1 + " cm\n"
        bodyText += "Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.XAlignedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.XAlignedCylinder(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_length=float(self.radius1),
                        cylinder_radius=float(self.radius2))
        return [local_shield]


class YCylinderShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Y-Aligned Cylinder"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Length: " + self.radius1 + " cm\n"
        bodyText += "Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.YAlignedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.YAlignedCylinder(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_length=float(self.radius1),
                        cylinder_radius=float(self.radius2))
        return [local_shield]


class ZCylinderShield(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Z-Aligned Cylinder"

    def summarize(self) -> str:
        bodyText = "Name: " + self.name + "\n"
        bodyText += "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Length: " + self.radius1 + " cm\n"
        bodyText += "Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = self.name + \
            "=shield.ZAlignedCylinder('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_shield = \
            shield.ZAlignedCylinder(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_length=float(self.radius1),
                        cylinder_radius=float(self.radius2))
        return [local_shield]


class SphereSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Sphere"
        self.shell = None

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Location: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Radius: " + self.radius1 + " cm\n"
        if self.shell is not None:
            bodyText += "Shell: \n"
            bodyText += self.shell.summarize()
        else:
            bodyText += "Shell: None \n"
        return bodyText

    def code(self) -> str:
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

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.SphereSource(self.material,
                          density=float(self.density),
                          sphere_center=[float(self.vector1[0]),
                                         float(self.vector1[1]),
                                         float(self.vector1[2])],
                          sphere_radius=float(self.radius1))
        if self.shell is not None:
            local_shell = \
                shield.Shell(self.shell.material,
                             sphere=local_source,
                             density=float(self.shell.density),
                             thickness=float(self.shell.thickness))
            return [local_source, local_shell]
        return [local_source]


class BoxSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Box"

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Box Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Dimensions: " + \
            self.vector2[0] + " cm, " + \
            self.vector2[1] + " cm, " + \
            self.vector2[2] + " cm\n"
        return bodyText

    def code(self) -> str:
        code = "my_source" + "=source.BoxSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", box_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", box_dimensions=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.BoxSource(self.material,
                       density=float(self.density),
                       box_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                       box_dimensions=[float(self.vector1[0]),
                                       float(self.vector1[1]),
                                       float(self.vector1[2])])
        return [local_source]


class XCylinderSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "X-Aligned Cylinder"

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Length: " + self.radius1 + " cm\n"
        bodyText += "Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = "my_source" + \
            "=source.XAlignedCylinderSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.XAlignedCylinderSource(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_length=float(self.radius1),
                        cylinder_radius=float(self.radius2))
        return [local_source]


class YCylinderSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Y-Aligned Cylinder"

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Length: " + self.radius1 + " cm\n"
        bodyText += "Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = "my_source" + \
            "=source.YAlignedCylinderSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.YAlignedCylinderSource(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_length=float(self.radius1),
                        cylinder_radius=float(self.radius2))
        return [local_source]


class ZCylinderSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Z-Aligned Cylinder"

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Material: " + self.material + "\n"
        bodyText += "Density: " + self.density + " g/cm3\n"
        bodyText += "Cylinder Center: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Length: " + self.radius1 + " cm\n"
        bodyText += "Radius: " + self.radius2 + " cm\n"
        return bodyText

    def code(self) -> str:
        code = "my_source" + \
            "=source.ZAlignedCylinderSource('" + self.material + "'" + \
            ", density=" + self.density + \
            ", cylinder_center=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", cylinder_length=" + self.radius1 + \
            ", cylinder_radius=" + self.radius2 + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.ZAlignedCylinderSource(self.material,
                       density=float(self.density),
                       cylinder_center=[float(self.vector1[0]),
                                   float(self.vector1[1]),
                                   float(self.vector1[2])],
                        cylinder_length=float(self.radius1),
                        cylinder_radius=float(self.radius2))
        return [local_source]


class PointSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Point"

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Location: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        return bodyText

    def code(self) -> str:
        code = "my_source" + "=source.PointSource(" + \
            "x=" + self.vector1[0] + \
            ", y=" + self.vector1[1] + \
            ", z=" + self.vector1[2] + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.PointSource(x=float(self.vector1[0]),
                               y=float(self.vector1[1]),
                               z=float(self.vector1[2]))
        return [local_source]


class LineSource(ShieldData):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Line"

    def summarize(self) -> str:
        bodyText = "Type: " + self.description + "\n"
        bodyText += "Starting Location: " + \
            self.vector1[0] + " cm, " + \
            self.vector1[1] + " cm, " + \
            self.vector1[2] + " cm\n"
        bodyText += "Ending Location: " + \
            self.vector2[0] + " cm, " + \
            self.vector2[1] + " cm, " + \
            self.vector2[2] + " cm\n"
        return bodyText

    def code(self) -> str:
        code = "my_source" + "=source.LineSource(" + \
            ", start=[" + self.vector1[0] + \
            ", " + self.vector1[1] + \
            ", " + self.vector1[2] + "]" + \
            ", end=[" + self.vector2[0] + \
            ", " + self.vector2[1] + \
            ", " + self.vector2[2] + "]" + ")"
        return code

    def phalax(self) -> list[shield.Shield]:
        local_source = \
            source.LineSource(start=[float(self.vector1[0]),
                               float(self.vector1[1]),
                               float(self.vector1[2])],
                              end=[float(self.vector1[0]),
                               float(self.vector1[1]),
                               float(self.vector1[2])])
        return [local_source]
