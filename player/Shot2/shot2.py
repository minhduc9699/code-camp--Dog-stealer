import game_object
import pygame
from game_object import GameObject

from physic.box_collider import BoxCollider


class Shot2(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/player-bullet.png")
        self.box_collider = BoxCollider(20, 20)
        self.vx = vx
        self.vy = vy

    def update(self):
        GameObject.update(self)
        self.y += self.vy
        self.x += self.vx
        self.deactivate_if_needed()
        # self.physics()

    def deactivate_if_needed(self):
        if (720 < self.y < 0):
            self.deactivate()
        if (1280 < self.x < 0):
            self.deactivate()

    def physics(self):
        if self.is_active:
          pass
