import pygame


class InputManager:
    def __init__(self):
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.left_mouse_clicked = False
        self.right_mouse_clicked = False
        self.x = 0
        self.y = 0

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.up_pressed = True
            elif event.key == pygame.K_DOWN:
                self.down_pressed = True
            elif event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.up_pressed = False
            elif event.key == pygame.K_DOWN:
                self.down_pressed = False
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = False
        
        ml, mm, mr = pygame.mouse.get_pressed()

        if ml:
          self.left_mouse_clicked = True
        else: 
          self.left_mouse_clicked = False
        if mr:
          self.right_mouse_clicked = True
        else:
          self.right_mouse_clicked = False
        
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)