import pygame
from constants import *

class ScoreLabel(pygame.sprite.Sprite):
  def __init__(self, x=0, y=0, w=150, h=30, text=""):
    super().__init__()
    self.text = text
    self.font = pygame.font.Font("freesansbold.ttf", 30)
    self.score = 0
    self.image = pygame.Surface((w, h))
    self.rect = self.image.get_rect(topleft=(x, y))

  def draw(self, screen):
    self.image.fill("#202020")
    text_surface = self.font.render(self.text, True, "#FFFFFF")
    self.image.blit(text_surface, (0, 0))
    screen.blit(self.image, self.rect)

  def update_score(self, score):
    self.score = score
    self.text = f"Score: {self.score}"
