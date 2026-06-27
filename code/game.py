import pygame

from code.const import MENU_OPTION
from code.const import WIN_HEIGHT
from code.const import WIN_WIDTH
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                from code.level import Level
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass
