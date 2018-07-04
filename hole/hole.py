import pygame
import game_object
from game_object import GameObject
from physic.box_collider import BoxCollider
from enemy.enemy import Enemy
from player.player import Player

class Hole(GameObject):
  def __init__(self, x, y):
    GameObject.__init__(self, x, y)
    self.image = pygame.image.load("./images/hole.png")
    self.box_collider = BoxCollider(50, 50)

  def update(self):
    GameObject.update(self)
    self.physic()

  def physic(self):
    if self.is_active:
      enemy = game_object.collide_with(self.box_collider, Enemy)
      player = game_object.collide_with(self.box_collider, Player)
      if enemy is not None:
        enemy.deactivate()
      if player is not None:
        # player.image = pygame.image.load("./images/enemy/virrut.png")
        pass
        




  

  
