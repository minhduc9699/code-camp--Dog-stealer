import pygame
from game_object import GameObject
from input_manager.input_manager import InputManager


class Mouse(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.input_manager = InputManager()
        self.left = pygame.image.load("images/left.png")
        self.right = pygame.image.load("images/right.png")
        self.all = pygame.image.load("images/all.png")
        self.image = self.all

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.x = mouse_x
        self.y = mouse_y
