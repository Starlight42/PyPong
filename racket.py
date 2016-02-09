import pygame
from constant import *

class Racket():
    def __init__(self, screen: pygame.Surface, size=4):
        self.size = size
        self.screen = screen
        self.screen_h = self.screen.get_height()
        self.screen_w = self.screen.get_width()
        self.img = pygame.image.load(RACKET_P1).convert_alpha()
        self.pos = [5, (self.screen_h - self.img.get_height()) // 2]

    def render(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, SCREEN_W, SCREEN_H))
        self.screen.blit(self.img, self.pos)
        print("Racket img height : {}".format(self.img.get_height()))
        print("Racket size : {}".format(self.img.get_size()))
        print("Racket pos : {}".format(self.pos))

    def move(self, vec: int=STALL):
        print("Racket Pos x : {}\nRacket Pos y : {}".format(self.pos[0], self.pos[1]))
        if vec == UP:
            if self.pos[1] - RACKET_SPEED >= 0:
                self.pos[1] -= RACKET_SPEED
            else:
                self.pos[1] = 0
        elif vec == DOWN:
            if self.pos[1] + RACKET_SPEED <= (self.screen_h - self.img.get_height()):
                self.pos[1] += RACKET_SPEED
            else:
                self.pos[1] = self.screen_h - self.img.get_height()

    def collision(self, pos_ball: tuple, ball_size: tuple):
        pass
