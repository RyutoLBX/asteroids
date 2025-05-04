import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(20, 50)
    split_vel_1 = self.velocity.rotate(angle)
    split_vel_2 = self.velocity.rotate(-angle)
    new_rad = self.radius - ASTEROID_MIN_RADIUS
    ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
    ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
    ast_1.velocity = split_vel_1 * 1.2
    ast_2.velocity = split_vel_2 *1.2