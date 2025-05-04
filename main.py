import pygame
from constants import *

def main() -> None:
  print("Starting Asteroids!")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # Clock definition
  cl = pygame.time.Clock()
  dt = 0.0

  # Game Loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("#000000")
    pygame.display.flip()
    dt = cl.tick(60)/1000

if __name__ == "__main__":
  main()