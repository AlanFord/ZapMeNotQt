#!/bin/bash

# Directory containing .ui files
DIRECTORY="."

# Loop through each .ui file in the directory
for ui_file in "$DIRECTORY"/*.ui; do
    # Check if the file exists
    if [ -f "$ui_file" ]; then
        # Get the base name of the file (without extension)
        base_name=$(basename "$ui_file" .ui)
        # Convert .ui to .py using uic
        uv run pyuic6 "$ui_file" -o "$DIRECTORY/$base_name.py"
        echo "Converted $ui_file to $base_name.py"
    else
        echo "No .ui files found in the directory."
    fi
done
