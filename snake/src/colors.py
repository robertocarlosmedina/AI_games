__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

from enum import Enum

class Game_color(Enum):
    blue = (0, 0, 255)
    white = (255, 255, 255)
    white1 = (155, 155, 155)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    green_1 = (0, 208, 28)
    green_2 = (0, 255, 34)
    green_3 = (137, 255, 0)
    black = (25, 25, 25)
    grey = (105, 105, 105)
    grey1 = (35, 35, 35)
    red = (255, 0, 0)


# this is to return the RGB value of the color
def rgbColor(co):
    return [color_e.value for color_name, color_e in Game_color.__members__.items() if co == color_name][0]