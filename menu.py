import pygame
from pygame.locals import *

from base_class.base_loop import BaseLoop
from constant import *


class MainMenu(BaseLoop):
    def __init__(self, screen: pygame.Surface):
        super(MainMenu, self).__init__(screen)
        self.font = pygame.font.SysFont('FreeSans', 12)

    def setup(self):
        super(MainMenu, self).setup()

    def update_screen(self):
        super(MainMenu, self).update_screen()
        text = self.font.render('Hello Master!', True, WHITE)
        self.screen.blit(text, (320, 240))

    def process_event(self, event: pygame.event):
        if event.type == KEYDOWN:
            pass

        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            self.LOOP_RUN = False
    
    def start(self):
        super(MainMenu, self).start()

        while self.LOOP_RUN:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()
            pygame.display.flip()
