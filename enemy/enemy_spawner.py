import pygame
from frame_counter import FrameCounter
from enemy.enemy import Enemy
import game_object
from game_object import GameObject
import game_object

class EnemySpawner(GameObject):
    def __init__(self,spawn_x,spawn_y):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(300)
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y

    def update(self):
        self.counter.run()

        if self.counter.expired: 
            enemy = self.spawn()
            # game_object.add(enemy)
            self.counter.reset()
        

    def spawn(self):
        return game_object.recycle(Enemy, self.spawn_x, self.spawn_y)