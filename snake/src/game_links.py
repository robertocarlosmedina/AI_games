__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

from typing import overload
import pygame
from src.pause_menu import Game_Pause_Menu
from src.game_lost import Game_Lost
from src.game_won import Game_won
from src.game import Game_loop
from src.start import Game_start
from src.menu import Game_menu
from src.quit import Game_quit
from src.tutorial import Game_Turorial 


class Game_links:
    game_page_object :object
    game_backup :object

    def __init__(self) -> None:
        self.game_page_object = object
        self.game_backup = object

    def start_game(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_start)):
            self.game_page_object = Game_start(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_main_menu(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_menu)):
            self.game_page_object = Game_menu(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def continue_game(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(isinstance(self.game_backup, Game_loop)):
            self.game_page_object = self.game_backup
        
        if(not isinstance(self.game_page_object, Game_loop)):
            self.game_page_object = Game_loop(screen, screen_size)

        return  self.game_page_object.run_link(game_event)

    def gameplay_loop(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_loop)):
            self.game_page_object = Game_loop(screen, screen_size)
        
        next_page = self.game_page_object.run_link(game_event)

        if (next_page != "game_loop"):
            self.game_backup = self.game_page_object

        return  next_page

    def game_tutorial(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_Turorial)):
            self.game_page_object = Game_Turorial(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_quit(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_quit)):
            self.game_page_object = Game_quit(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_pause_menu(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_Pause_Menu)):
            self.game_page_object = Game_Pause_Menu(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_won(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_won)):
            self.game_backup = object
            self.game_page_object = Game_won(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_lost(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_Lost)):
            self.game_backup = object
            self.game_page_object = Game_Lost(screen, screen_size)
        return  self.game_page_object.run_link(game_event)