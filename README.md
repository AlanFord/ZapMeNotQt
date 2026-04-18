ZapMeNotQt

A front-end for ZapMeNot written in Qt for Python.  ZapMeNotQt provides a GUI interface
to assist in writing ZapMeNot Python scripts.  A ZapMeNot Python script defines a photon
shielding model consisting of, at a minimum, a source and a detector.  The script may also
include descriptions of one or more photon shields.

To run ZapMeNotQt using uv:
Install uv and then use the command:  uv run src/ZapMeNot/ZapMeNotQt.py

To build an installer:  uv run pyinstaller ZapMeNotQt.spec

General Design

The main window will display a summary of the shielding model as it is constructed.  The display will be user-friendly, summarizing the user's input as it is created.  A graphical display will be generated on-demand in a separate window that must be closed to continue.  Another window will display a ZapMeNot script generated from the user input.  This window also provides the capability to save the ZapMeNot Python script is a file with a name determined by the user.  This window must be closed to return back to the main window.
