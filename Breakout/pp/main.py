import pygame, sys
from settings import *
from player import Player,Enemy
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.sprite.GroupSingle(Player(30,'Crimson'))
ball = pygame.sprite.GroupSingle(Ball())
clock = pygame.time.Clock()
enemy = pygame.sprite.GroupSingle(Enemy(screen_width - 30,'Violet'))
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#0d031f')
    player.draw(screen)
    player.update()
    pygame.draw.ellipse(screen, "White", ball.sprite)
    ball.update(player.sprite,enemy.sprite)
    enemy.draw(screen)
    enemy.update(ball.sprite)

    pygame.display.update()