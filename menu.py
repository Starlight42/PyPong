import pygame
from pygame.locals import *

from base_class.base_loop import BaseLoop
from menu_item import MenuItem
from game import Game
from constant import *


class MainMenu(BaseLoop):
    def __init__(self, screen: pygame.Surface):
        super(MainMenu, self).__init__(screen)
        self.game = Game(self.screen)
        screen_portion = (self.screen.get_width() / 2, self.screen.get_height() / 3)
        screen_portion1 = (screen_portion[0], screen_portion[1] * 1.5)
        screen_portion2 = (screen_portion[0], screen_portion[1] * 2)

        self.menu = [MenuItem(self.screen, '1 PLAYER', screen_portion),
                     MenuItem(self.screen, '2 PLAYER', screen_portion1),
                     MenuItem(self.screen, 'QUIT MENU', screen_portion2)]

    def setup(self):
        super(MainMenu, self).setup()
        self.menu[0].select(True)

    def update_screen(self):
        super(MainMenu, self).update_screen()
        for item in self.menu:
            if item.selected:
                item.render(RED)
            else:
                item.render(BLUE)

    def find_select(self, direction):
        for index, menu in enumerate(self.menu):
            if menu.selected:
                menu.select(False)
                if direction is UP:
                    self.menu[index - 1].select(True)
                elif direction is DOWN:
                    self.menu[0 if (index+1) == len(self.menu) else index + 1].select(True)
                break

    def process_event(self, event: pygame.event):
        if event.type == KEYDOWN:
            if event.key == CONTROLS[UP]:
                self.find_select(UP)
            elif event.key == CONTROLS[DOWN]:
                self.find_select(DOWN)
            elif event.key == K_RETURN:
                self.game.start()

        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            self.LOOP_RUN = False
    
    def start(self):
        super(MainMenu, self).start()

        while self.LOOP_RUN:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()
            pygame.display.flip()
