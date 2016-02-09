import pygame
from pygame.locals import *
from game import Game
from constant import (SCREEN_SIZE, SCREEN_ORI,
                      BG_PATH, BLACK)

def main():
    print("Press return to start the game")

    pygame.init()
    RUN = True
    screen = pygame.display.set_mode(SCREEN_SIZE)
    background = pygame.image.load(BG_PATH).convert_alpha()
    game = Game(screen)

    while RUN:
        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                RUN = False
            if event.type == KEYDOWN and event.key == K_RETURN:
                game.start()

        pygame.draw.rect(screen, BLACK, (0, 0) + SCREEN_SIZE)
        screen.blit(background, SCREEN_ORI)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
