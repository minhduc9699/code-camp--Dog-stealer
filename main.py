import pygame
import game_object
from input_manager.input_manager import InputManager
BG_COLOR = (125, 125, 0)

#1. init pygame
pygame.init()

#2. setup screen
size = (1024, 600)
canvas = pygame.display.set_mode(size)
input_manager = InputManager()
clock = pygame.time.Clock()

loop = True
while loop:
  #loop events
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      loop = False
    input_manager.update(event)
  
  game_object.update()
  canvas.fill(BG_COLOR)

  game_object.render(canvas)
 

  pygame.display.flip()
  clock.tick(60)


