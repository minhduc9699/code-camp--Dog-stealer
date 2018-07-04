import pygame
import game_object
import pygame
import game_object
from game_object import GameObject
from physic.box_collider import BoxCollider
from player.player import Player

class Shop(GameObject):
  def __init__(self, x, y):
    GameObject.__init__(self, x, y)
    self.image = pygame.image.load("./images/hole.png")
    self.box_collider = BoxCollider(50, 50)

  def update(self):
    GameObject.update(self)
    self.physic()

  def physic(self):
    if self.is_active:
      player = game_object.collide_with(self.box_collider, Player)
      if player is not None and player.has_dog:
        print("hit")
        player.has_dog = False


