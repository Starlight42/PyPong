import pygame
from constant import *


class BaseLoop:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.LOOP_RUN = True

    def setup(self):
        self.LOOP_RUN = True
        pygame.key.set_repeat(200, 50)

    def update_screen(self):
        pygame.draw.rect(self.screen, BLACK, SCREEN_ORI + SCREEN_SIZE)

    def process_event(self, event: pygame.event):
        pass

    def start(self):
        self.setup()
