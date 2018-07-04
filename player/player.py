import pygame
from player.player_bullet import *
import game_object
from game_object import GameObject
from frame_counter import FrameCounter


class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.image = pygame.image.load("./images/player/player1.png")
        self.shoot_lock = False
        self.counter = FrameCounter(20)

    def update(self):
        self.move()
        self.shoot()

    def move(self):
        dx = 0
        dy = 0
        step = 7
        if self.input_manager.up_pressed:
            dy -= step
        if self.input_manager.down_pressed:
            dy += step
        if self.input_manager.left_pressed:
            dx -= step
        if self.input_manager.right_pressed:
            dx += step
        self.x += dx
        self.y += dy

    def shoot(self):
        if self.input_manager.x_pressed and not self.shoot_lock:
            bullet = game_object.recycle(PlayerBullet, self.x, self.y - 25)
            self.shoot_lock = True

        if self.shoot_lock:
            self.counter.run()
            if self.counter.expired:
                self.shoot_lock = False
                self.counter.reset()


import game_object
from game_object import GameObject
from frame_counter import FrameCounter
from player.Shot1.shot1 import Shot1
from quick_math import get_distance
from physic.box_collider import BoxCollider
from dog.dog import Dog


class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.image = pygame.image.load("images/player/player1.png")
        self.counter1 = FrameCounter(120)
        self.counter2 = FrameCounter(120)
        self.shoot_lock1 = False
        self.shoot_lock2 = False
        self.box_collider = BoxCollider(70, 70)

    def update(self):
        GameObject.update(self)
        self.move()
        self.shoot_left()
        self.shoot_right()
        self.physics()

    def move(self):
        dx = 0
        dy = 0
        step = 5

        if self.input_manager.up_pressed:
            dy -= step
        if self.input_manager.down_pressed:
            dy += step
        if self.input_manager.left_pressed:
            dx -= step
        if self.input_manager.right_pressed:
            dx += step

        self.x += dx
        self.y += dy

    def shoot_left(self):
        if self.input_manager.left_mouse_clicked and not self.shoot_lock1:
            self.shoot_lock1 = True
            # print('left hitu')
            # game_object.recycle(Shot1)
            try:
                distance = (get_distance((self.x, self.y),
                                         (self.input_manager.mouse_x, self.input_manager.mouse_y)))
                shot1 = game_object.recycle(Shot1, self.x, self.y)
                shot1.velocity = ((self.input_manager.mouse_x - self.x) / distance * 5,
                                  (self.input_manager.mouse_y - self.y) / distance * 5)
            except ZeroDivisionError:
                # game_object.add(shot1)
                pass

        if self.shoot_lock1:
            self.counter1.run()
            if self.counter1.expired:
                self.shoot_lock1 = False
                self.counter1.reset()
        # pass

    def shoot_right(self):
        if self.input_manager.right_mouse_clicked and not self.shoot_lock2:
            self.shoot_lock2 = True
            # print('right Hitu')
        if self.shoot_lock2:
            self.counter2.run()
            if self.counter2.expired:

                self.shoot_lock2 = False
                self.counter2.reset()

    def physics(self):
        if self.is_active:
            shot1 = game_object.collide_with(self.box_collider, Shot1)
            if shot1 is not None and shot1.returning:
                shot1.deactivate()
            dog = game_object.collide_with(self.box_collider, Dog)
            if dog is not None and dog.returning:
                dog.deactivate()
