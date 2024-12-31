import sys

import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    my_font = pygame.font.SysFont("monospace", 40)
    score = 0
    lives = 3

    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    score += 10
                    print(f"Score: {score}")
                    asteroid.split()
                    shot.kill()

            if asteroid.check_collision(player):
                player.kill()
                lives -= 1
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                updatable.add(player)
                drawable.add(player)
                print(f"Lives: {lives}")
                print("You Died")

                if lives == 0:
                    print("Game Over!")
                    sys.exit()

        score_text = f"Score: {score}"
        score_text_surface = my_font.render(score_text, True, (255, 255, 255))

        lives_text = f"{lives * "▲ "}"
        lives_text_surface = my_font.render(lives_text, True, (255, 255, 255))


        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        screen.blit(score_text_surface, (20,20))
        screen.blit(lives_text_surface, (20,SCREEN_HEIGHT - lives_text_surface.get_height() - 20))

        pygame.display.flip()


        # framerate = 60 FPS
        dt = clock.tick(60) / 1000.0



if __name__ == "__main__":
    main()