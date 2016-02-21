import pygame

from base_class.base_object import BaseObject
from constant import *


class Racket(BaseObject):
    def __init__(self, screen: pygame.Surface, size=4, mode=None):
        super(Racket, self).__init__(screen)
        self.mode = mode
        self.size = size
        self.paddle = pygame.draw.rect(self.screen, BLUE, (0, 0, 20, 80))
        self.screen_h = self.screen.get_height()
        self.screen_w = self.screen.get_width()
        self.pos = [5 if mode is None else (self.screen_w-(5+self.paddle.width)),
                    (self.screen_h - self.paddle.height) // 2]


    def render(self):
        self.paddle = pygame.draw.rect(self.screen, BLUE, (self.pos[0], self.pos[1], 20, 80))

    def move(self, vec: int=STALL):
        if vec == UP:
            if self.pos[1] - RACKET_SPEED >= 0:
                self.pos[1] -= RACKET_SPEED
            else:
                self.pos[1] = 0
        elif vec == DOWN:
            if self.pos[1] + RACKET_SPEED <= (self.screen_h - self.paddle.height):
                self.pos[1] += RACKET_SPEED
            else:
                self.pos[1] = self.screen_h - self.paddle.height

    def auto_move(self, ball):
        if ball.vec[0] == -1:
            if self.paddle.centery < (self.screen_h/2):
                self.pos[1] += 1
            elif self.paddle.centery > (self.screen_h/2):
                self.pos[1] -= 1
        elif ball.vec[0] == 1:
            if self.paddle.centery < ball.ball.centery:
                self.pos[1] += 1
            else:
                self.pos[1] -= 1

    def collision(self, pos_ball: tuple, ball_size: tuple):
        pass
