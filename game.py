import pygame
from pygame.locals import *

from ball import Ball
from base_class.base_loop import BaseLoop
from constant import *
from racket import Racket


class Game(BaseLoop):
    def __init__(self, screen: pygame.Surface):
        super(Game, self).__init__(screen)
        self.FPSCLOCK = None
        self.racket_p1 = Racket(self.screen)
        self.ball = Ball(self.screen)

    def setup(self):
        super(Game, self).setup()
        self.FPSCLOCK = pygame.time.Clock()
        self.racket_p1 = Racket(self.screen)
        self.ball = Ball(self.screen)

    def update_screen(self):
        super(Game, self).update_screen()
        pygame.draw.rect(self.screen, WHITE, ((self.screen.get_width() // 2) - 1, 0, 2,
                                              self.screen.get_height()))
        self.racket_p1.render()
        self.ball.render()

    def process_event(self, event: pygame.event):
        if event.type == KEYDOWN:
            if event.key == CONTROLS[UP]:
                self.racket_p1.move(UP)
            elif event.key == CONTROLS[DOWN]:
                self.racket_p1.move(DOWN)

        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            self.LOOP_RUN = False
            print('Ending the game...')

    def start(self, game_type="one_player"):
        print('Starting the game...')
        super(Game, self).start()

        while self.LOOP_RUN:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()
            self.ball.move(self.racket_p1)
            pygame.display.flip()
            self.FPSCLOCK.tick(FPS)
