from os import write
import pygame
from src.colors import Game_color as color
from src.font import Game_fonts as fonts

surface = pygame.Surface((100, 100))
file :object
file_data :str

def draw_header_styled_lines(screen :pygame.Surface, screen_size :tuple) -> None:
    pygame.draw.line(
        screen, 
        color.green.value,
        (screen_size[0]/2 - 190, 100), 
        (screen_size[0]/2 + 190, 100), 
        3
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 - 180, 95), 
        (screen_size[0]/2 + 180, 95),  
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 - 180, 105), 
        (screen_size[0]/2 + 180, 105), 
        1
    )

def draw_vertical_styled_lines(screen :pygame.Surface, screen_size :tuple) -> None:
    pygame.draw.line(
        screen, 
        color.green.value,
        (screen_size[0]/2 , 140), 
        (screen_size[0]/2, 430), 
        3
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 - 7 , 150), 
        (screen_size[0]/2 - 7, 420), 
        
    )
    pygame.draw.line(
        screen, 
        color.grey.value,
        (screen_size[0]/2 + 7, 150), 
        (screen_size[0]/2 + 7, 420), 
        1
    )

def display_game_snake_info(screen :pygame.Surface, info_name :str, value :int, position :dict) -> None:
    font_size :int
    surface.fill(color.black.value)
    pygame.draw.rect(
        surface , 
        color.green.value, 
        pygame.Rect(1,1, 98,98),
        1
    )
    font_size = pygame.font.Font.size(fonts.montserrat_small_font.value, f"{value}")
    line = fonts.montserrat_small_font.value.render(f"{value}", True, color.white.value)
    surface.blit(line, (50-font_size[0] / 2, 30))
    font_size = pygame.font.Font.size(fonts.montserrat_super_small_font.value, f"{info_name}")
    line = fonts.montserrat_super_small_font.value.render(f"{info_name}", True, color.white.value)
    surface.blit(line, (50-font_size[0]/2, 60))
    screen.blit(surface, (position["x"], position["y"]))

def read_from_file(file_path :str, mode :str, clean_data :bool) -> list:
    file = open(file_path, mode)
    file_data = file.readlines()
    file.close()
    
    if clean_data:
        file = open(file_path, "w")
        file.close()

    return file_data

def write_from_file(file_path :str, mode :str, value :str) -> None:
    file = open(file_path, mode)
    file.write(value)
    file.close()
