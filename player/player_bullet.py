import pygame
import game_object
from game_object import GameObject
from physic.box_collider import BoxCollider
from enemy.enemy import Enemy

class PlayerBullet(GameObject):
  def __init__(self, x, y):
    GameObject.__init__(self, x, y)
    self.image = pygame.image.load("images/player-bullet.png")
    self.box_collider = BoxCollider(20, 20)


  def update(self):
    GameObject.update(self)
    self.y -= 10
    self.deactivate_if_needed()
    self.physic()

  
  def physic(self):
    if self.is_active:
      enemy = game_object.collide_with(self.box_collider, Enemy)
      if enemy is not None:
        enemy.deactivate()
        self.deactivate()

  

  def deactivate_if_needed(self):
    if self.y < 0:
      self.deactivate()
