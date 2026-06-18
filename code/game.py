import pygame
from code.menu import Menu
from code.const import WINDOW_HEIGHT
from code.const import WINDOW_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pg.event.get():
            # if event.type == pg.QUIT:
            # pg.quit()  # Close Window
            # quit()  # End Pygame
