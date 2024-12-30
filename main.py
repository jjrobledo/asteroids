import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        # framerate = 60 FPS
        dt = clock.tick(60) / 1000.0



if __name__ == "__main__":
    main()