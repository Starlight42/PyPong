import pygame
from base_class.base_object import BaseObject
from constant import *
from racket import Racket


class Ball(BaseObject):
    def __init__(self, screen: pygame.Surface):
        super(Ball, self).__init__(screen)
        self.img = pygame.image.load(BALL).convert_alpha()
        self.vec = [-1, -1]
        self.ball_h = self.img.get_height()
        self.ball_w = self.img.get_width()
        self.pos = [(self.screen.get_width() - self.ball_w) // 2,
                    (self.screen.get_height() - self.ball_h) // 2]

    def check_edge_collision(self):
        if self.pos[1] <= 0 or self.pos[1] >= SCREEN_H - self.ball_h:
            self.vec[1] *= -1
        if self.pos[0] >= SCREEN_W - self.ball_w or self.pos[0] <= 0:
            self.vec[0] *= -1

    def check_racket_collision(self, racket: Racket):
        pass
        #if self.pos[1] == racket.pos[1] and self.pos[0] == racket.pos[0]:
        #   self.vec[1] *= -1
        #if self.pos[0] == racket.pos[0]:
        #   self.vec[0] *= -1

    def move(self, racket: Racket):
        self.check_edge_collision()

        self.pos[0] += self.vec[0]
        self.pos[1] += self.vec[1]
