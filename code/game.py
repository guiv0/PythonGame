import sys

import pygame

from code.const import MENU_OPTION
from code.const import WIN_HEIGHT
from code.const import WIN_WIDTH
from code.level import Level
from code.menu import Menu
from code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run()
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run()
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[2]:
                score.show()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
