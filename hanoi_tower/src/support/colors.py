__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    All the available color's that can be used on the game.
"""

from enum import Enum

class Game_color(Enum):
    blue = (0, 55, 255)
    blue_1 = (0, 11, 171)
    blue_2 = (0, 94, 182)
    dark_blue = (0, 6, 97)
    white = (255, 255, 255)
    white_1 = (205, 205, 205)
    white_2 = (155, 155, 155)
    white_3 = (105, 105, 105)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    darck_green = (9, 129, 0)
    green_1 = (0, 208, 28)
    green_2 = (0, 255, 34)
    green_3 = (137, 255, 0)
    black = (25, 25, 25)
    grey = (105, 105, 105)
    grey_1 = (35, 35, 35)
    red = (255, 0, 0)
    red_1 = (255, 132, 132)
    red_2 = (192, 0, 0)
    brown_1 = (52, 25, 0)
    brown = (129, 91, 1)

# this is to return the RGB value of the color
def rgbColor(co):
    return [color_e.value for color_name, color_e in Game_color.__members__.items() if co == color_name][0]