import pygame
import game_object
from game_object import GameObject
from frame_counter import FrameCounter
from player.Shot1.shot1 import Shot1
from quick_math import get_distance
from physic.box_collider import BoxCollider
from dog.dog import Dog
from player.Shot2.shot2 import Shot2

# from main import mouse

class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.image = pygame.image.load("images/player/player1.png")
        self.counter1 = FrameCounter(120)
        self.counter2 = FrameCounter(120)
        self.has_shoot1 = True
        self.has_shoot2 = True
        self.dog_count = 0
        self.box_collider = BoxCollider(70, 70)


    def update(self):
        GameObject.update(self)
        self.move()
        self.shoot_left()
        self.shoot_right()
        self.physics()
        # if self.has_shoot1 and self.has_shoot2:
        #     mouse.image = mouse.all
        # elif self.has_shoot1:
        #     mouse.image = mouse.left
        # elif self.has_shoot2:
        #     mouse.image = mouse.right

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
        if self.input_manager.left_mouse_clicked and self.has_shoot1:
            self.has_shoot1 = False
            # print('left hitu')
            # game_object.recycle(Shot1)
            try:
                distance = (get_distance((self.x, self.y),
                                         (self.input_manager.mouse_x, self.input_manager.mouse_y)))
                shot1 = game_object.recycle(Shot1, self.x, self.y)
                shot1.velocity = ((self.input_manager.mouse_x - self.x) / distance * 5,
                                  (self.input_manager.mouse_y - self.y) / distance * 5)
                shot1.counter.reset()
            except ZeroDivisionError:
                # game_object.add(shot1)
                pass

        # pass

    def shoot_right(self):
        if self.input_manager.right_mouse_clicked and self.has_shoot2:
            self.has_shoot2 = False
            
            try:
                distance = (get_distance((self.x, self.y),
                                         (self.input_manager.mouse_x, self.input_manager.mouse_y)))
                shot2 = game_object.recycle(Shot2, self.x, self.y -10)
                shot2.velocity = ((self.input_manager.mouse_x - self.x) / distance * 10,
                                  (self.input_manager.mouse_y - self.y) / distance * 10)
                shot2.time_before_disappear.reset()
            except ZeroDivisionError:
                # game_object.add(shot1)
                pass
        if self.has_shoot2 == False:
            self.counter2.run()
            if self.counter2.expired:
                self.has_shoot2 = True
                self.counter2.reset()

    def physics(self):
        if self.is_active:
            shot1 = game_object.collide_with(self.box_collider, Shot1)
            if shot1 is not None and shot1.returning:
                self.has_shoot1 = True
                shot1.deactivate()
                
            # dog = game_object.collide_with(self.box_collider, Dog)
            # if dog is not None and dog.returning:
            #     self.dog_count += 1
            #     dog.deactivate()

            