#!/usr/bin/env bash
if [ "$#" -ne 1 ]; then
    echo "Error: Provide a python file as argument 1."
    exit 1
fi
file_path="$1"
extension="${1##*.}"
jupyter_path="${1%.*}.ipynb"

if [ "${extension}" != "py" ]; then
    echo "Error: Please provide a python file."
    exit 1
fi


marimo export ipynb "$file_path" -o "$jupyter_path"
