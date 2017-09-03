import pygame
from constant import *


class MenuItem:
    def __init__(self, screen: pygame.Surface, text, item_center, item_size: tuple=None):
        self.screen = screen
        self.rect_dim = (300, 50) if item_size is None else item_size
        self.text = text
        self.selected = False
        self.text_render = None
        self.font = pygame.font.SysFont('FreeSansBold', 42)
        self.rect = pygame.Rect(SCREEN_ORI, self.rect_dim)
        self.text_dim = self.font.size(self.text)
        self.rect_center = item_center
        self.pos_text = (self.rect_center[0] - (self.text_dim[0] / 2),
                         self.rect_center[1] - (self.text_dim[1] / 2))

    def render(self, text_color: tuple=BLACK):
        self.rect.center = self.rect_center
        self.screen.fill(WHITE, self.rect)
        self.text_render = self.font.render(self.text, True, text_color)
        self.screen.blit(self.text_render, self.pos_text)

    def select(self, is_selected: bool):
        self.selected = is_selected
        self.font = pygame.font.SysFont('FreeSansBold', 42, italic=is_selected)
