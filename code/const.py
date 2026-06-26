# C
import pygame
from setuptools.errors import PlatformError

COLOR_WHITE = (244, 244, 244)
COLOR_BLUE = (120, 120, 255)
COLOR_RED = (120, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BROWN = (77, 58, 0)

# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}
EVENT_ENEMY = pygame.USEREVENT + 1
# M
MENU_OPTION = ('New Game - 1 Player',
               'New Game - 2 Players',
               'Score',
               'Quit Game')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 5000
# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
