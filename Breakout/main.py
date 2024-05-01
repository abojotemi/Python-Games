import pygame, sys
from player import Player

from tile import Tile
from ball import Ball
from settings import *
from random import choice
pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
game_on = False
start = True
font = pygame.font.SysFont('Jetbrains Mono', 30)


player = pygame.sprite.GroupSingle()
ball = pygame.sprite.GroupSingle()
obs = pygame.sprite.Group()
def add_enemy():
    player.add(Player())
    ball.add(Ball(player))
    for i in range(5):
        for j in range(15):
            obs.add(Tile((64*j,16*i),choice(colors),ball))
add_enemy()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_on:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    obs.empty()
                    player.empty()
                    ball.empty()
                    add_enemy()
                    game_on = True
                    start = False
        elif game_on:
            if event.type == pygame.KEYDOWN and ball.sprite.direction.y == 0:
                ball.sprite.direction.y = -1
    if game_on:
        if ball.sprite.rect.top >= screen_height:
            game_on = False
        screen.fill('#0d031f')
        player.draw(screen)
        player.update()
        obs.draw(screen)
        obs.update()
        ball.draw(screen)
        ball.update()
            
    else:
        if start:
            text = font.render('Click spacebar to start',True, '#9f7f6f')

        else:
            text = font.render("GAME OVER", True, 'White')
        text_rect = text.get_rect(center = (screen_width/2,screen_height/2))
        screen.blit(text,text_rect)
            

            
#9f7f6f

    pygame.display.update()