This folder contains the Qt Designer files for the ZapMeNotQt application.  Each .ui file holds the design of a main window, window, dialog box, or widget.  

The files can be converted to python files using the "convert.sh" bash script.
The script is designed to be used along with the PyQt6 Python package.  It can 
be converted to use the alternative PySide6 Python package by changing the
call to pyuic6 to be a call to pyside6-uic.

A good reference and tutorial for loading .ui files and/or converting these
files to Python is
"Creating GUI Applications with Python and Qt6 (PyQt6 Edition)" by Martin Fitzpatrick.