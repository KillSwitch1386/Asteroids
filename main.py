# this allows us to use code from
# the open-source pygame library
# throughout this file
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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.check_for_collision(shot):
                    asteroid.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        

        dt = clock.tick(MAX_FPS) / 1000
        


if __name__ == "__main__":
    main()