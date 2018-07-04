import pygame
from game_object import GameObject;

BLUE = (0,0, 255)

class BoxCollider(GameObject):
  def __init__(self, width, height):
    GameObject.__init__(self, 0, 0)
    self.width = width
    self.height = height

  def conners(self):
    
    return (
            self.x - self.width / 2,
            self.x + self.width / 2,
            self.y - self.height / 2,
            self.y + self.height / 2
            )

  def collide_with(self, other):
    left1, right1, top1, bot1 = self.conners()
    left2, right2, top2, bot2 = other.conners()

    x_overlap = right2 >= left1 and left2 <= right1
    y_overlap = top2 >= bot1 and bot2 <= top1

    return x_overlap and y_overlap
  

  def render(self, canvas):
    pygame.draw.rect(canvas, 
    BLUE,
    (self.x - self.width / 2,
     self.y - self.height / 2, self.width, self.height ),
    1)

