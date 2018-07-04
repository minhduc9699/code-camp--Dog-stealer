import pygame
import game_object
from frame_counter import FrameCounter
from game_object import GameObject
from dog.dog import Dog

class DogSpawner(GameObject):
  def __init__(self, x, y):
    GameObject.__init__(self, x, y)
    self.frame_counter = FrameCounter(400)

  def update(self):
    self.frame_counter.run()

    if self.frame_counter.expired:
      dog = self.spawn()
      self.frame_counter.reset()

  def spawn(self):
    return game_object.recycle(Dog, self.x, self.y)