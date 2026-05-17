ZapMeNotQt (A Work in Progress)

This is in development and is not a completely functional project.

ZapMeNotQt is a GUI front-end for ZapMeNot written in Qt for Python.  ZapMeNotQt provides a GUI interface to assist in writing ZapMeNot Python scripts.  A ZapMeNot Python script defines a photon shielding model consisting of, at a minimum, a source and a detector.  The script may also include descriptions of one or more photon shields.

ZapMeNotQt 
- assists in developing the shielding model
- generates a ZapMeNot script describing the model
- plots the shielding geometry for visual review
- runs the shielding calculation and presents the results

To run ZapMeNotQt using uv:
Install uv and then use the command:  uv run src/ZapMeNotQt.py

Note that ZapMeNotQt requires access to a ZapMeNot wheel.  The location of the ZapMeNot wheel
must be specified in the pyproject.toml file.  If ZapMeNot package has been installed, remove
the location of the ZapMeNot wheel from the pyproject.toml file.

Any ZapMeNot commit dated on or after 5/10/2026 is compatible with ZapMeNotQt

To build an installer:  uv run pyinstaller ZapMeNotQt.spec

To typecheck with ty:  uvx ty check

To lint with ruff: uv run ruff check . 
