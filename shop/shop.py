import pygame
import game_object
import pygame
import game_object
from game_object import GameObject
from physic.box_collider import BoxCollider
from player.player import Player
from dog.dog import Dog


class Shop(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("./images/hole.png")
        self.box_collider = BoxCollider(50, 400)

    def update(self):
        GameObject.update(self)
        self.physic()

    def physic(self):
        # if self.is_active:
        player = game_object.collide_with(self.box_collider, Player)
        dog = game_object.collide_with(self.box_collider, Dog)
        if player is not None and player.dog_count > 0:
            print(player.dog_count)
            player.dog_count = 0

        if dog is not None and dog.is_active:
            print('hit')
            dog.deactivate()
