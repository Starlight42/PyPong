import pygame
from racket import Racket
from constant import *

class Ball():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.img = pygame.image.load(BALL).convert_alpha()
        self.vec = [-BALL_SPEED, BALL_SPEED]
        self.ball_h = self.img.get_height()
        self.ball_w = self.img.get_width()
        self.pos = [(self.screen.get_width() - self.ball_w) // 2,
                    (self.screen.get_height() - self.ball_h) // 2]

    def render(self):
        self.screen.blit(self.img, self.pos)

    def move(self, racket: Racket):
        pass
