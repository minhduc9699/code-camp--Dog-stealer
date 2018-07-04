import pygame
from frame_counter import FrameCounter
from enemy.enemy import Enemy
import game_object
from game_object import GameObject
import game_object

class EnemySpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(120)

    def update(self):
        self.counter.run()

        if self.counter.expired: 
            enemy = self.spawn()
            # game_object.add(enemy)
            self.counter.reset()
        

    def spawn(self):
        return game_object.recycle(Enemy, 200, 300)