import pygame
from base_class.base_object import BaseObject
from constant import *
from racket import Racket


class Ball(BaseObject):
    def __init__(self, screen: pygame.Surface):
        super(Ball, self).__init__(screen)
        self.ball = pygame.draw.circle(self.screen, WHITE, (320, 240), BALL_RADIUS)
        self.vec = [-1, -1]
        self.ball_h = self.ball.height
        self.ball_w = self.ball.width
        self.pos = [(self.screen.get_width() - self.ball_w) // 2,
                    (self.screen.get_height() - self.ball_h) // 2]

    def check_edge_collision(self):
        if self.pos[1] <= (self.ball.height/2) or self.pos[1] >= SCREEN_H - (self.ball.height/2):
            self.vec[1] *= -1
        if self.pos[0] >= SCREEN_W - (self.ball_w/2) or self.pos[0] <= (self.ball.width/2):
            self.vec[0] *= -1

    def render(self):
        self.ball = pygame.draw.circle(self.screen, WHITE, (self.pos[0], self.pos[1]), BALL_RADIUS)

    def check_racket_collision(self, racket_p1: Racket, racket_p2: Racket):
        if self.vec[0] == -1 and racket_p1.paddle.right == self.ball.left and \
                        racket_p1.paddle.top < self.ball.top and \
                        racket_p1.paddle.bottom > self.ball.bottom:
            self.vec[0] *= -1
        elif self.vec[0] == 1 and racket_p2.paddle.left == self.ball.right:
            self.vec[0] *= -1

    def move(self, racket_p1: Racket, racket_p2=None):
        self.check_edge_collision()
        self.check_racket_collision(racket_p1, racket_p2)

        self.pos[0] += self.vec[0]
        self.pos[1] += self.vec[1]
