import os

# Screen property
SCREEN_H = 480
SCREEN_W = 640
SCREEN_SIZE = (SCREEN_W, SCREEN_H)
SCREEN_ORI = (0, 0)

# Assets property
ASSETS_DIR = "assets/"
BG_PATH = os.path.join(os.getcwd(), ASSETS_DIR + 'Start_screen.jpg')
RACKET_P1 = os.path.join(os.getcwd(), ASSETS_DIR + 'Racket_p1.png')
BALL = os.path.join(os.getcwd(), ASSETS_DIR + 'Ball.png')

# Racket property
STALL = -1
UP = 0
DOWN = 1
RACKET_SPEED = 20  # In pixel/second
BALL_SPEED = 4  # In pixel/second
