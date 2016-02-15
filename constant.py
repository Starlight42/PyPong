import os
from pygame.locals import K_UP, K_DOWN

# Game settings constant
FPS = 350

# Screen constant
SCREEN_H = 480
SCREEN_W = 640
SCREEN_SIZE = (SCREEN_W, SCREEN_H)
SCREEN_ORI = (0, 0)

# Assets constant
ASSETS_DIR = 'assets/'
BG_PATH = os.path.join(os.getcwd(), ASSETS_DIR + 'Start_screen.jpg')
RACKET_P1 = os.path.join(os.getcwd(), ASSETS_DIR + 'Racket_p1.png')
BALL = os.path.join(os.getcwd(), ASSETS_DIR + 'Ball.png')

# Racket constant
STALL = -1
UP = 0
DOWN = 1
RACKET_SPEED = 20  # In pixel/second
BALL_SPEED = 20  # In pixel/second

# keys constant
CONTROLS = {
    UP: K_UP,
    DOWN: K_DOWN
}

# Menu item constant
MENU_ITEMS = {
    0: "one_player",
    1: "two_player",
    2: "quit"
}

# Color constant
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
