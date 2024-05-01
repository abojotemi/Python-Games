from settings import *
from random import randint, choice
import pygame 
opps = choice(['Bald Guy','Cucumber','Whale'])
class Enemy(pygame.sprite.Sprite):

    def __init__(self,game,pos,group):
        super().__init__(group)
        opps = choice(['Bald Guy','Cucumber','Whale'])
        
        self.game = game
        self.image_dict = {}
        self.image_dict['_left'],self.image_dict['_right'] = load_images(f"assets/{opps}/Run")
        self.image = self.image_dict['_left'][0]
        self.rect = self.image.get_rect(topleft = (pos[0],pos[1]+TILE_SIZE))
        self.facing_left = True if opps in ('Cucumber','Whale') else False
         
        if opps == 'Whale':
            self.rect.y += 20
        self.state  = '_left' if self.facing_left else '_right'
        self.speed = randint(4,6)
        self.animation_speed = 0.2
        self.index = 0
        self.animation_index = 0
        self.ex_animation_speed = 0.5
        self.direction = -1
        self.death_trigger = False
        self.timer = 0
    def animate(self):
        self.state = '_left' if self.facing_left else '_right'
        self.index += self.animation_speed
        self.image = self.image_dict[self.state][int(self.index)%len(self.image_dict[self.state])]
    
    def explosion_animation(self):
        self.animation_index  += self.ex_animation_speed
        if self.animation_index < len(explosion):
                self.image = explosion[int(self.animation_index)]
                self.rect = self.image.get_rect(center = self.rect.center)
    def collide_with_rect(self, group):
        for sprite in group:
            if self.rect.colliderect(sprite.rect):
                self.direction *= -1
                self.facing_left = not self.facing_left
    def collide_with_player(self,player,bombs):
        if self.rect.colliderect(player.rect):
            if player.velocity > 1 and player.in_air:
                player.velocity = -14
                self.death_trigger = True
                self.direction = 0
            elif self.game.current_time - self.timer > 1000 and abs(player.velocity) < 1:
                self.timer = pygame.time.get_ticks()
                if len(self.game.health)==1:
                    player.is_dead = True
                    player.is_alive = False
                    try:
                        self.game.health.pop()
                    except:
                        pass
                elif len(self.game.health) > 1:
                    self.game.health.pop()
            if self.game.current_time - self.timer < 2000 and player.state_pre != 'Hit':
                player.is_hit = True
        for sprite in bombs:
            if self.rect.colliderect(sprite.rect):
                self.direction = 0
                self.death_trigger = True
                sprite.kill()
        if self.death_trigger :
            self.explosion_animation()
            if self.animation_index >= len(explosion):
                self.kill()
    def update(self,group,player,bombs):
        self.rect.x += self.direction * self.speed
        self.animate()
        self.collide_with_rect(group)
        self.collide_with_player(player,bombs)



class Bomb(pygame.sprite.Sprite):

    def __init__(self, position, state,collision_tiles,group,player):
        super().__init__(group)
        self.index = 0
        self.explosion_index = 0
        self.image = bombs[self.index]
        self.animation_speed = 0.3
        self.explosion_animation_speed = 0.3
        self.collision_tiles = collision_tiles
        self.mask = pygame.mask.from_surface(self.image)
        if state == 'left':
            self.rect = self.image.get_rect(bottomright = position)
            self.x = -randint(3,5) + player.frame_movement//2
        elif state == 'right':
            self.rect = self.image.get_rect(bottomleft = position)
            self.x = randint(3,5)+player.frame_movement//2
        

        self.initial_velocity = -randint(2,5)
    def animate(self):
        self.index += self.animation_speed
        self.image = bombs[int(self.index)% len(bombs)]
    
    def explosion_animation(self):
        self.explosion_index += self.explosion_animation_speed
        if self.explosion_index < len(bomb_explosion):
            self.image = bomb_explosion[int(self.explosion_index)]
            self.rect = self.image.get_rect(center = self.rect.center)
            self.initial_velocity = 0
            self.x = 0
    
    def movement(self):
        self.rect.x += self.x
        self.initial_velocity += 0.1
        self.rect.y += self.initial_velocity
        for tile in self.collision_tiles:
            if self.rect.colliderect(tile.rect):
                self.explosion_animation()
                if self.explosion_index >= len(bomb_explosion):
                    self.kill()
    def update(self):
        self.animate()
        self.movement()
        if self.rect.bottom > 1000:
            self.kill()