import pygame
from racket import Racket
from constant import *
from base_object import BaseObject
from random import randint

class Ball(BaseObject):
    def __init__(self, screen: pygame.Surface):
        super(Ball, self).__init__(screen)
        self.img = pygame.image.load(BALL).convert_alpha()
        self.vec = [-1, -1]
        self.ball_h = self.img.get_height()
        self.ball_w = self.img.get_width()
        self.pos = [(self.screen.get_width() - self.ball_w) // 2,
                    (self.screen.get_height() - self.ball_h) // 2]

    def move(self, racket: Racket):
        if self.pos[1] <= 0 or self.pos[1] >= SCREEN_H - self.ball_h:
            self.vec[1] *= -1
        if self.pos[0] >= SCREEN_W - self.ball_w or self.pos[0] <= 0:
            self.vec[0] *= -1

        if self.pos[1] == racket.pos[1] and self.pos[0] == racket.pos[0]:
            self.vec[1] *= -1
        #if self.pos[0] == racket.pos[0]:
        #   self.vec[0] *= -1

        self.pos[0] += self.vec[0]
        self.pos[1] += self.vec[1]
