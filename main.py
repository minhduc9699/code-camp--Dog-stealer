import pygame
import game_object
from hole.hole import Hole
from player.player import Player
from input_manager.input_manager import InputManager
from enemy.enemy import Enemy
from dog.dog import Dog
from enemy.enemy_spawner import EnemySpawner
from dog.dog_spawner import DogSpawner
from shop.shop import Shop
from mouse import Mouse
BG_COLOR = (125, 125, 0)

# 1. init pygame
pygame.init()

# 2. setup screen
size = (1280, 720)
canvas = pygame.display.set_mode(size)
input_manager = InputManager()

hole = Hole(680, 360)
shop = Shop(1200, 360)
player = Player(2, 3, input_manager)
dog_spawner = DogSpawner(500, 500)
# enemy_spawner1 = EnemySpawner(200,300)
# enemy_spawner2 = EnemySpawner(100,100)
enemy = Enemy(500, 500)
game_object.add(player)
game_object.add(hole)
game_object.add(dog_spawner)
# game_object.add(enemy_spawner1)
game_object.add(enemy)
game_object.add(shop)
mouse = Mouse(0, 0)
game_object.add(mouse)

clock = pygame.time.Clock()

loop = True
while loop:
    # loop events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        input_manager.update(event)
    game_object.update()
    game_object.position = (player.x, player.y)

    if player.has_shoot1 and player.has_shoot2:
        mouse.image = mouse.all
    elif player.has_shoot1:
        mouse.image = mouse.left
    elif player.has_shoot2:
        mouse.image = mouse.right

    game_object.update()
    canvas.fill(BG_COLOR)

    game_object.render(canvas)

    pygame.display.flip()
    clock.tick(60)
