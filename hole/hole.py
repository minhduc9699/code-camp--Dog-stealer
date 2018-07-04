import pygame
from game_object import GameObject
from physic.box_collider import BoxCollider

class Hole(GameObject):
  def __init__(self, x, y):
    GameObject.__init__(self, x, y)
    # self.image = pygame.image.load("")
    self.box_collider = BoxCollider(35, 35)

  def physic(self):
    if self.is_active:
      enemy = game_object.collide_with(self.box_collider, Enemy)
      if enemy is not None:
        enemy.deactivate()
        self.deactivate()

  def deactivate_if_needed(self):
    if self.y < 0:
      self.deactivate()
