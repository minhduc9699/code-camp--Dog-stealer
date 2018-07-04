import game_object
import pygame
from game_object import GameObject

from physic.box_collider import BoxCollider
from dog.dog import Dog
from quick_math import get_distance
from frame_counter import FrameCounter
# from game_object import position


class Shot1(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/player-bullet.png")
        self.box_collider = BoxCollider(40, 40)
        self.velocity = (0, 0)
        self.returning = False
        self.counter = FrameCounter(120)

    def update(self):
        GameObject.update(self)
        self.move()
        self.deactivate_if_needed()
        self.physics()
        self.return_to_player()

    def move(self):
        self.vx, self.vy = self.velocity
        self.y += self.vy
        self.x += self.vx
        self.counter.run()
        if self.counter.expired:
          self.returning = True
          self.counter.reset()

    def deactivate_if_needed(self):
        if self.y < 0 or self.y > 720:
            self.deactivate()
        if self.x < 0 or self.x > 1280:
            self.deactivate()

    def physics(self):
        if self.is_active:
            hit_object = game_object.collide_with(self.box_collider, Dog)
            if hit_object is not None:
                # self.deactivate()
                # dog.deactivate()
                self.returning = True
                hit_object.returning = True

    def return_to_player(self):
        if self.is_active and self.returning:
            try:
                px, py = game_object.position
                distance = (get_distance((self.x, self.y),
                                         (px, py)))
                self.velocity = ((-px + self.x) / distance * -5,
                                 (-py + self.y) / distance * -5)
            except ZeroDivisionError:
                pass

    def clean(self):
        self.returning = False
        self.velocity = (0, 0)
