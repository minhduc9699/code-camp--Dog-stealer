import pygame
import game_object
from physic.box_collider import BoxCollider
from game_object import GameObject
from frame_counter import FrameCounter
from random import randint

class Enemy(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.image = pygame.image.load("images/enemy/bacteria1.png")
        self.box_collider = BoxCollider(40,40)
        self.counter = FrameCounter(70)

    def update(self):
        GameObject.update(self)
        self.follow_player()
 
    def follow_player(self):
        px,py = game_object.position
        if (self.x < px):
            self.x += 1
            if (self.y < py):
                self.y += 1
            else:
                self.y -= 1
        else:
            self.x -= 1
            if (self.y < py):
                self.y +=1
            else:
                self.y -= 1

