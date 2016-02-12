import pygame

class BaseObject():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.pos = []
        self.img = None

    def render(self):
        self.screen.blit(self.img, self.pos)
