# define a pattern rule to convert ui files to py files
all: *.py
.PHONY: all

%.py : %.ui
	uv run pyuic6 $< -o $@
