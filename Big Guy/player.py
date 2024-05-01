import pygame, os
from pygame import Vector2 as vector
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, position,group, collision_sprites,surface):
        super().__init__(group)
        self.display_surface = surface
        #Image_state
        self.state_pre = 'Idle'
        self.is_facing_left = False
        self.state_suf = '_right'
        self.state = self.state_pre + self.state_suf
        self.image_dict = load_images("assets/Big Guy",True)
        
        self.index = 0
        self.throw_index = 0
        self.hit_index = 0
        self.image = self.image_dict[self.state][self.index]
        self.rect = self.image.get_rect(center = position)
        self.mask = pygame.mask.from_surface(self.image)
        self.throw = False
        self.is_hit = False
        self.is_dead = False
        self.dead_index = 0
        self.is_alive = True

        #Dust
        self.dust_run = dust_particles['Run']
        self.dust_jump = dust_particles['Jump']
        self.dust_land = dust_particles['Fall']
        self.dust_index = 0
        self.dust_animation_speed = 0.3
        self.jump_index = 0
        self.land_index = 0
        self.land_pos = self.rect.midbottom
            
        
        #Collisions
        self.tiles = collision_sprites.sprites()
        self.offset = vector()

        #Movement
        self.movement = vector()
        self.speed = 8
        self.velocity = 0
        self.gravity = 1

        #Position state
        self.on_floor = False
        self.in_air = False
        self.on_left = False
        self.on_right = False
        self.player_pos = 0
        self.k_space = False
        
        #Coin
        self.coin_count = 0
        

    #Movement
    def move(self):
        self.frame_movement = (self.movement.y - self.movement.x) * self.speed
        self.rect.x += self.frame_movement
        if self.frame_movement < 0:
            self.is_facing_left = True
        elif self.frame_movement > 0:
            self.is_facing_left = False
        
        
    #Collisions
    def horizontal_collisions(self):
        for tile in self.tiles:
            if tile.rect.colliderect(self.rect):
                if self.frame_movement > 0:
                    self.rect.right = tile.rect.left
                    self.on_left = True
                    self.player_pos = self.rect.center
                if self.frame_movement < 0:
                    self.rect.left = tile.rect.right
                    self.on_right = True
                    self.player_pos = self.rect.center
        if self.rect.center != self.player_pos:
            self.on_left,self.on_right = False,False
    def vertical_collisions(self):
        for tile in self.tiles:
            if tile.rect.colliderect(self.rect):
                if self.velocity > 0:
                    self.on_floor = True
                    self.in_air = False
                    self.rect.bottom = tile.rect.top
                    self.jump_pos = self.rect.midbottom
                    if self.velocity > 2:
                        self.land_pos = self.rect.midbottom  - self.offset - vector(45,40)
                        self.land_index = 0
                    self.velocity = 0
                if self.velocity < 0:
                    self.velocity = 0
                    self.rect.top = tile.rect.bottom
            if abs(self.velocity) > 1:
                self.on_floor = False
                self.in_air = True
                
    def apply_gravity(self):
        self.velocity += self.gravity
        # self.velocity = min(self.velocity, 9)
        self.rect.y += self.velocity
        
    #Player state
    def state_select(self):
        if self.is_hit:
            self.state_pre = 'Hit'
        elif self.throw:
            self.state_pre = 'Throw'
        elif self.on_floor and self.frame_movement == 0:
            self.state_pre = 'Idle'
            
        elif self.on_floor and self.frame_movement != 0:
            self.state_pre = 'Run'
            
        
        elif not self.on_floor and self.velocity < 0:
            self.state_pre = 'Jump'
        
        elif not self.on_floor and self.velocity > 0:
            self.state_pre = 'Fall'        
    
    #animations
    def animate(self):
        self.index += 0.2
        if not self.throw and not self.is_hit and not self.is_dead:
            self.image = self.image_dict[self.state][(int(self.index))%len(self.image_dict[self.state])]
        elif self.throw:
            self.throw_index += 0.8
            if self.throw_index >= len(self.image_dict[self.state]):
                self.throw = False
                self.throw_index = 0
            self.image = self.image_dict[self.state][int(self.throw_index)]
        elif self.is_dead:
            self.state_pre = 'DeadHit'
            self.dead_index += 0.2
            if self.dead_index >= len(self.image_dict[self.state]):
                
                self.state_pre = 'Dead'
                self.image = self.image_dict[self.state][int(self.dead_index)%len(self.image_dict[self.state])]
            else:
                self.image = self.image_dict[self.state][int(self.dead_index)]
        elif self.is_hit:
            self.hit_index += 0.3
            if self.hit_index >= len(self.image_dict[self.state]):
                self.is_hit = False
                self.hit_index = 0
            self.image = self.image_dict[self.state][int(self.hit_index)]
                
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        self.state_suf = '_left' if self.is_facing_left else '_right'
        self.state = self.state_pre + self.state_suf
    def run_animate(self):
        if self.state_pre == 'Run':
            self.dust_index += self.dust_animation_speed
            surf = self.dust_run[int(self.dust_index)%len(self.dust_run)]
            offset = vector(30,0)
            if self.is_facing_left:
                
                surf_rect = surf.get_rect(midbottom = self.rect.bottomright - self.offset)#- offset)
                self.display_surface.blit(pygame.transform.flip(surf,1,0),surf_rect)
            elif not self.is_facing_left:
                surf_rect = surf.get_rect(midbottom = self.rect.bottomleft - self.offset)#+offset)
                self.display_surface.blit(surf,surf_rect)
    def jump_animate(self):
        if self.state_pre == 'Jump' and self.k_space:
            self.jump_index += self.dust_animation_speed
            if self.jump_index < len(self.dust_jump):
                offset = vector(45,40)
                surf = self.dust_jump[int(self.jump_index)%len(self.dust_jump)]
                rect = self.jump_pos - self.offset - offset
                self.display_surface.blit(surf,rect)
    def land_animate(self):
        if self.on_floor:
            self.land_index += self.dust_animation_speed
            if self.land_index < len(self.dust_land):
                # offset = vector(45,65)
                surf = self.dust_land[int(self.land_index)%len(self.dust_land)]
                rect = self.land_pos #- offset
                self.display_surface.blit(surf,rect)
    
    def update(self):
        self.state_select()
        self.animate()
        if self.is_alive:
            self.move()
            self.horizontal_collisions()
            self.run_animate()        
            self.land_animate()
            self.jump_animate()
        self.apply_gravity()
        self.vertical_collisions()
        if self.velocity > 0:
            self.k_space = False
        if self.rect.top > WINDOW_HEIGHT:
            self.rect.bottom = -10
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 3864:
            self.rect.right = 3864