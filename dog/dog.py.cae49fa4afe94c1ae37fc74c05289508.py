import game_object
import pygame
import random
from game_object import GameObject

from physic.box_collider import BoxCollider
from quick_math import get_distance
from frame_counter import FrameCounter


class Dog(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/enemy.png")
        self.box_collider = BoxCollider(100, 100)
        self.returning = False
        self.velocity = (0, 0)
        self.counter = FrameCounter(100)
        self.spawn_lock = False

        # not stun
        self.stun_timer = FrameCounter(90)
        self.stun_timer.count = 90

    def update(self):
        GameObject.update(self)
        self.move()
        if not self.pushed:
            self.decide_movement()
        self.return_to_player()

    def move(self):

        if self.stun_timer.expired:
            # input movement here
            self.velocity = (0,0)
            pass
        else:
            self.stun_timer.run()


        self.vx, self.vy = self.velocity
        self.y += self.vy
        self.x += self.vx
        if self.x >= 1270:
            self.x = 1270
        if self.x <= 10:
            self.x = 10
        if self.y >= 710:
            self.y = 710
        if self.y <= 10:
            self.y = 10

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
        self.velocity = (0, 0)
        self.returning = False
        self.pushed = False

    def decide_movement(self):
        if not self.spawn_lock:
            self.spawn_lock = True

        if self.spawn_lock:
            self.counter.run()
            if self.counter.expired:
                self.spawn_lock = False
                self.counter.reset()
