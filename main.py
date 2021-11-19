import os
from typing import List

from fontforge import *



input_folder: str = os.path.join(os.getcwd(), "input\\")  # Path to input & output relative to the current working directory
output_folder: str = os.path.join(os.getcwd(), "output\\")

if not os.path.exists(input_folder):
    os.mkdir(input_folder)

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

fonts: List[fontforge.font] = [
    open(os.path.join(input_folder, font_name))
    for font_name
    in os.listdir(input_folder)  # All .ttf folders
]

for font in fonts:
    for glyph in font:
        font_relative_path: str = f"{font.fontname}\\"
        if not os.path.exists(os.path.join(output_folder, font_relative_path)):
            os.mkdir(os.path.join(output_folder, font_relative_path))
        if font[glyph].isWorthOutputting():
            glyph_file_name: str = font[glyph].glyphname + ".png"
            try:
                font[glyph].export(os.path.join(output_folder, font_relative_path, glyph_file_name))
            except OSError:
                continue
