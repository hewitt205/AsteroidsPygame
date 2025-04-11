import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *

def main():
    gameOn = True
    while(gameOn):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    pygame.Surface.fill(screen, (0,0,0))

    pygame.dispplay.flip() #display updated screen - run at end of loop
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main()
