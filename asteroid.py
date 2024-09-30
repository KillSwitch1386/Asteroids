import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            split_angle = random.uniform(20, 50)
            split_vector_1 = self.velocity.rotate(split_angle)
            split_vector_2 = self.velocity.rotate(-split_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
            new_asteroid_1.velocity = split_vector_1 * 1.2
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
            new_asteroid_2.velocity = split_vector_2 * 1.2