import pygame
from pygame.locals import *
from game import Game
from constant import *

def main():
    print("Press any key to start the game")

    pygame.init()
    RUN = True
    GAME_STATE = False
    screen = pygame.display.set_mode(SCREEN_SIZE)
    background = pygame.image.load(BG_PATH).convert_alpha()
    game = Game(screen)

    while RUN:

        if not GAME_STATE:
            screen.blit(background, SCREEN_ORI)
        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                RUN = False
            if event.type == KEYDOWN and event.key == K_RETURN:
                #if not GAME_STATE:
                GAME_STATE = True
                game.start()

        #screen.blit(background, SCREEN_ORI)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
