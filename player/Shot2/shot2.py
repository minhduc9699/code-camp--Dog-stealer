import game_object
import pygame
from game_object import GameObject

from physic.box_collider import BoxCollider
from dog.dog import Dog
from quick_math import get_distance
from frame_counter import FrameCounter
# from game_object import position
from enemy.enemy import Enemy
from quick_math import get_distance


class Shot2(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/player-bullet.png")
        self.box_collider = BoxCollider(60, 60)
        self.velocity = (0, 0)
        self.time_before_disappear = FrameCounter(20)

    def update(self):
        GameObject.update(self)
        self.move()
        self.physics()

    def move(self):
        self.vx, self.vy = self.velocity
        self.y += self.vy
        self.x += self.vx

        self.time_before_disappear.run()
        if self.time_before_disappear.expired:
            self.deactivate()

    def physics(self):
        if self.is_active:

            dog = game_object.collide_with(self.box_collider, Dog)
            if dog is not None:
                # self.deactivate()
                # dog.deactivate()
                distance1 = get_distance((self.x, self.y), (dog.x, dog.y))
                dog.velocity = ((dog.x - self.x) / distance1 *
                                10, (dog.y - self.y) / distance1 * 10)
                dog.stun_timer.reset()
                dog.returning = False

            enemy = game_object.collide_with(self.box_collider, Enemy)
            if enemy is not None:
                distance2 = get_distance((self.x, self.y), (enemy.x, enemy.y))
                enemy.velocity = ((enemy.x - self.x) / distance2 * 20,
                                  (enemy.y - self.y) / distance2 * 20)
                enemy.stun_timer.reset()
                enemy.returning = False

    def clean(self):
        self.returning = False
        self.velocity = (0, 0)
