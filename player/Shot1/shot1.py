import game_object
import pygame
from game_object import GameObject

from physic.box_collider import BoxCollider
from dog.dog import Dog
from quick_math import get_distance
from frame_counter import FrameCounter
# from game_object import position
from enemy.enemy import Enemy


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
        self.physics()
        self.return_to_player()

    def move(self):
        self.vx, self.vy = self.velocity
        self.y += self.vy
        self.x += self.vx
        # self.counter.reset()
        self.counter.run()
        if self.counter.expired:
            self.returning = True
            self.counter.reset()

    def physics(self):
        if self.is_active:
            dog = game_object.collide_with(self.box_collider, Dog)
            if dog is not None:
                # self.deactivate()
                # dog.deactivate()
                self.returning = True
                dog.returning = True

            enemy = game_object.collide_with(self.box_collider, Enemy)
            if enemy is not None:
                self.returning = True
                enemy.returning = True

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
