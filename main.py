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
    game_over = False

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


        if not game_over:

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
                        game_over = True
                        player.kill()

        score_text = f"Score: {score}"
        score_text_surface = my_font.render(score_text, True, (255, 255, 255))

        lives_text = f"{lives * "▲ "}"
        lives_text_surface = my_font.render(lives_text, True, (255, 255, 255))


        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        screen.blit(score_text_surface, (20,20))
        screen.blit(lives_text_surface, (20,SCREEN_HEIGHT - lives_text_surface.get_height() - 20))

        if game_over:
            player.kill()
            gameover_text = "Game Over"
            game_over_font = pygame.font.SysFont("monospace", 120)
            gameover_text_surface = game_over_font.render(gameover_text, True, (255, 255, 255))
            gameover_position = (
                (SCREEN_WIDTH - gameover_text_surface.get_width()) / 2,
                (SCREEN_HEIGHT - gameover_text_surface.get_height()) / 2
            )
            screen.blit(gameover_text_surface, gameover_position)

        pygame.display.flip()


        # framerate = 60 FPS
        dt = clock.tick(60) / 1000.0




if __name__ == "__main__":
    main()