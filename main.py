import pygame
import game_object
from player.player import Player
from input_manager.input_manager import InputManager
from dog.dog import Dog
BG_COLOR = (125, 125, 0)

#1. init pygame
pygame.init()

#2. setup screen
size = (1280, 720)
canvas = pygame.display.set_mode(size)
input_manager = InputManager()

player = Player(2, 3, input_manager)
dog = Dog(50, 50)
game_object.add(player)
game_object.add(dog)

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
  game_object.position = (player.x, player.y)
  

  canvas.fill(BG_COLOR)

  game_object.render(canvas)
 

  pygame.display.flip()
  clock.tick(60)


