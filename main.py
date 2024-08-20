import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    # Main Game Loop
    while True:
        # Exit code if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update objects on screen
        for obj in updatable:
            obj.update(dt)

        # Fill background to black
        screen.fill("black")

        # Draw objects to screen
        for obj in drawable:
            obj.draw(screen)
        
        # Check asteroid collision with player or shots
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        # Set to 60 frames per second and get delta time.
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()