import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scorelabel import ScoreLabel
from prettyprint import pretty_print, print_end_score

def main() -> None:
  pretty_print("Launching Asteroids!")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # Definitions
  cl = pygame.time.Clock()
  dt = 0.0

  score = 0
  score_label = ScoreLabel()
  score_label.update_score(score)

  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatables, drawables)
  Asteroid.containers = (asteroids, updatables, drawables)
  Shot.containers = (shots, updatables, drawables)
  AsteroidField.containers = (updatables)
  drawables.add(score_label)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  # Game Loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("#000000")
    dt = cl.tick(60) / 1000

    updatables.update(dt)

    for ast in asteroids:
      if player.is_colliding(ast):
        pretty_print("GAME OVER")
        print_end_score(score)
        sys.exit()

      for bullet in shots:
        if bullet.is_colliding(ast):
          score += 1
          score_label.update_score(score)
          ast.split()
          bullet.kill()

    for obj in drawables:
      obj.draw(screen)

    pygame.display.flip()
  # End of game loop

if __name__ == "__main__":
  main()