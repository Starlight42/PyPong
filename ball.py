import pygame
from racket import Racket
from constant import *
from random import randint

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
        tmp = self.pos[0] + self.vec[0] * BALL_SPEED, self.pos[1] + self.vec[1] * BALL_SPEED
        collision = racket.collision(tmp, (self.ball_w, self.ball_h))

        if collision or tmp[0] <= 0 or tmp[0] + self.ball_w >= self.screen.get_width():
            self.vec[0] = - self.vec[0] + randint(100, 255) / 1000
            self.vec[1] += randint(100, 255) / 1000
        if tmp[1] <= 0 or tmp[1] + self.ball_h >= self.screen.get_height():
            self.vec[0] += randint(100, 255) / 1000
            self.vec[1] = - self.vec[1] + randint(100, 255) / 1000

        self.pos[0] += self.vec[0]
        self.pos[1] += self.vec[1]
