ZapMeNotQt

A front-end for ZapMeNot written in Qt for Python.

General Design

The main window will display a summary of the shielding model as itis constructed.  The display will be user-friendly, not the Python script.  A graphical display will be generated on-demand in a separate window that must be closed to continue.  An other window will display the ZapMeNot script, but must be closed to continue.

The main window will have a menu with the following options:

- run
- detector location
- add source
	- material
	- quadrature
	- photons
		- isotope
		- by energy
- remove source
- add shield
- remove shield
- options
	- buildup factor material
	- fill material
	- use daughters