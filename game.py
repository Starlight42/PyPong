import pygame
from constant import *
from racket import Racket
from ball import Ball
from random import choice

class Game():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.racket_p1 = Racket(screen)
        #self.racket_p2 = Racket(screen)
        self.ball = Ball(screen)

    def start(self):
        self.racket_p1.render()
        self.ball.render()
        self.racket_p1.move(DOWN)
