import pygame
from pygame.locals import *
from constant import *
from racket import Racket
from ball import Ball

class Game():
    def __init__(self, screen: pygame.Surface):
        self.GAME_RUN = True
        self.FPSCLOCK = None
        self.screen = screen
        self.racket_p1 = Racket(self.screen)
        self.ball = Ball(self.screen)

    def setup(self):
        pygame.key.set_repeat(200, 50)
        self.FPSCLOCK = pygame.time.Clock()
        self.GAME_RUN = True
        self.racket_p1 = Racket(self.screen)
        self.ball = Ball(self.screen)

    def update_screen(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0) + SCREEN_SIZE)
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
            self.GAME_RUN = False
            print('Ending the game...')

    def start(self):
        print('Starting the game...')
        self.setup()

        while self.GAME_RUN:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()
            self.ball.move(self.racket_p1)
            pygame.display.flip()
            self.FPSCLOCK.tick(FPS)
