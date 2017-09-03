import pygame
from pygame.locals import *
from menu import MainMenu
from constant import (SCREEN_SIZE, SCREEN_ORI,
                      BG_PATH, BLACK)


def main():
    print('Press return to start the game')

    pygame.init()
    RUN = True
    screen = pygame.display.set_mode(SCREEN_SIZE)
    background = pygame.image.load(BG_PATH).convert_alpha()
    pygame.display.set_caption('PyPong')
    menu = MainMenu(screen)

    while RUN:
        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                RUN = False
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu.start()

        pygame.draw.rect(screen, BLACK, SCREEN_ORI + SCREEN_SIZE)
        screen.blit(background, SCREEN_ORI)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
