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
        self.racket_p2 = None
        self.ball = Ball(self.screen)

    def setup(self):
        super(Game, self).setup()
        pygame.key.set_repeat(100, 20)
        self.FPSCLOCK = pygame.time.Clock()
        self.racket_p1 = Racket(self.screen)
        self.ball = Ball(self.screen)
        self.racket_p2 = Racket(self.screen, mode='auto')

    def update_screen(self):
        super(Game, self).update_screen()
        pygame.draw.rect(self.screen, WHITE, ((self.screen.get_width() // 2) - 1, 0, 2,
                                              self.screen.get_height()))
        self.racket_p1.render()
        self.racket_p2.render()
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
        self.game_type = game_type
        super(Game, self).start()

        while self.LOOP_RUN:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()
            self.ball.move(self.racket_p1, self.racket_p2)
            self.racket_p2.auto_move(self.ball)
            pygame.display.flip()
            self.FPSCLOCK.tick(FPS)
