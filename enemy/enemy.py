import pygame
import game_object
from physic.box_collider import BoxCollider
from game_object import GameObject
from frame_counter import FrameCounter
from random import randint

from quick_math import get_distance


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/enemy/bacteria1.png")
        self.box_collider = BoxCollider(40, 40)
        self.counter = FrameCounter(70)
        self.returning = False
        self.velocity = (0, 0)
        self.pushed = False

        # not stun
        self.stun_timer = FrameCounter(20)
        self.stun_timer.count = 20

    def update(self):
        GameObject.update(self)
        self.move()

    def move(self):

        if self.stun_timer.expired:
            try:
                px, py = game_object.position
                distance = (get_distance((self.x, self.y),
                                         (px, py)))
                self.velocity = ((-px + self.x) / distance * -1,
                                 (-py + self.y) / distance * -1)
            except ZeroDivisionError:
                pass
        else:
            self.stun_timer.run()
            print(self.stun_timer.count)

        self.return_to_player()

        vx, vy = self.velocity
        # print(self.velocity)
        self.x += vx
        self.y += vy

    def return_to_player(self):
        if self.is_active and self.returning:
            try:
                px, py = game_object.position
                distance = (get_distance((self.x, self.y),
                                         (px, py)))
                # print(distance)
                self.velocity = ((-px + self.x) / distance * -4,
                                 (-py + self.y) / distance * -4)
            except ZeroDivisionError:
                pass

    def clean(self):
        self.velocity = (0, 0)
        self.returning = False
        self.pushed = False
