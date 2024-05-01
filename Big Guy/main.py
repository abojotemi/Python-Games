import pygame, sys
from pygame import Vector2 as vector
from csv import reader
from tiles import Tile
from settings import *
from player import Player
from enum import Enum
from camera import Camera
from classes import *
from random import randint
from interactives import *
class Game:
    def __init__(self):
        pygame.init()

#Screen settings
        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Your Game Title")

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.visible_sprites = Camera()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.bomb_tiles = pygame.sprite.Group()
        self.init_game()

    def init_game(self):
# Load game assets and initialize game state here
#		self.movement = pygame.Vector2(0,0)                   
        self.enemies = pygame.sprite.Group()  
        self.terrain = pygame.sprite.Group()  
        self.obstacles = pygame.sprite.Group()      
        self.clouds = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.make_clouds()
        self.coin_index = 0
        self.display_coin = gold_coins[self.coin_index]
        
        with open('assets/maps/level_obstacles.csv') as f:
            self.map_tiles = list(reader(f))
        
        for row_num, row in enumerate(self.map_tiles):
            for col_num ,cell in enumerate(row):
                if cell != '-1':
                    Tile((col_num * TILE_SIZE, row_num * TILE_SIZE),self.obstacles)
                    
        self.load_terrain_tiles('assets/maps/level_terrain.csv',NormalTile,[self.visible_sprites,self.collision_sprites])
        self.load_coins()
        self.load_enemy_tiles('assets/maps/level_Enemy.csv',Enemy,[self.enemies,self.visible_sprites])
        self.player = Player((200,200),[self.active_sprites,self.visible_sprites],self.collision_sprites,self.screen)
        self.font = pygame.font.Font('assets/fonts/ARCADEPI.ttf', 30)
        self.coin_count = self.font.render(f'Coins: {self.player.coin_count}',False,'Black')
        self.health = []
        self.coin_state = 'gold'
        self.set_timer = pygame.time.get_ticks()
        # self.rec = pygame.Rect(0,50,self.screen_width, 30)
        # Health((63,57),self.health)
        # Health((63+16,57),self.health)
        
        for i in range(8):
            self.health.append(Health((63+i*19,60)))
    def load_enemy_tiles(self,path,class_,group):
        with open(path) as f:
            self.tiles = list(reader(f))
        for row_num, row in enumerate(self.tiles):
            for col_num, cell in enumerate(row):
                if cell == '0':
                    class_(self,(col_num * TILE_SIZE,row_num * TILE_SIZE),group)

            
    def load_terrain_tiles(self,path,class_,group):
        with open(path) as f:
            self.tiles = list(reader(f))
        for row_num, row in enumerate(self.tiles):
            for col_num, cell in enumerate(row):
                if cell == '0':
                    class_(terrain_tiles[0][0],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '1':
                    class_(terrain_tiles[0][1],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '2':
                    class_(terrain_tiles[0][2],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '3':
                    class_(terrain_tiles[0][3],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '4':
                    class_(terrain_tiles[1][0],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '5':
                    class_(terrain_tiles[1][1],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '6':
                    class_(terrain_tiles[1][2],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '7':
                    class_(terrain_tiles[1][3],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '8':
                    class_(terrain_tiles[2][0],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '9':
                    class_(terrain_tiles[2][1],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '10':
                    class_(terrain_tiles[2][2],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '11':
                    class_(terrain_tiles[2][3],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '12':
                    class_(terrain_tiles[3][0],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '13':
                    class_(terrain_tiles[3][1],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '14':
                    class_(terrain_tiles[3][2],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
                if cell == '15':
                    class_(terrain_tiles[3][3],(col_num * TILE_SIZE,row_num * TILE_SIZE),group)
               
    def load_coins(self):
        with open('assets/maps/level_coins.csv') as f:
            tiles = list(reader(f))
        for row_num, row in enumerate(tiles):
            for col_num, cell in enumerate(row):
                if cell == '0':
                    Coin(self,gold_coins,(col_num * TILE_SIZE,row_num * TILE_SIZE),[self.visible_sprites,self.coins],'gold')
                if cell == '1':
                    Coin(self,silver_coins,(col_num * TILE_SIZE,row_num * TILE_SIZE),[self.visible_sprites,self.coins],'silver')
                   
            
    def make_clouds(self,):
        for i in range(randint(100,200)):
            Cloud(clouds[randint(0,2)],(randint(30,4000),randint(0, 450)), [self.visible_sprites,self.clouds])
        
        # for j in range(5,9):
        #     Cloud(ship,(randint(30,4000),randint(470, 500)), [self.visible_sprites,self.clouds])
            
            

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
        # Add event handling code here
            if event.type == pygame.KEYDOWN:
                if self.player.is_alive:
                    if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                            ...
                    if event.key == pygame.K_LEFT:
                        self.player.movement.x = 1
                        # self.player.is_facing_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.player.movement.y = 1
                        # self.player.is_facing_left = False
                    if event.key == pygame.K_SPACE:
                        if self.player.on_floor:
                            self.player.velocity = -24
                            self.player.jump_index = 0
                            self.player.k_space = True
                    if event.key == pygame.K_LSHIFT:
                        self.player.throw = True
                        if self.current_time - self.set_timer > 2000:
                            if self.player.state_suf == '_left':
                                
                                Bomb(self.player.rect.midright,'left',self.collision_sprites,[self.visible_sprites,self.bomb_tiles],self.player)
                            if self.player.state_suf == '_right':
                                
                                Bomb(self.player.rect.midleft,'right',self.collision_sprites,[self.visible_sprites,self.bomb_tiles],self.player)
                            self.set_timer = pygame.time.get_ticks()
                        
                        
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.movement.x = 0
                elif event.key == pygame.K_RIGHT:
                    self.player.movement.y = 0

        
    

    def update(self):
        #Update game logic here
        self.enemies.update(self.obstacles,self.player,self.bomb_tiles)
        self.active_sprites.update()
        self.clouds.update()
        self.bomb_tiles.update()
        self.coins.update(self.player)
        self.coin_count = self.font.render(f'{self.player.coin_count}',False,'Black')
        self.coin_index += 0.2
        self.display_coin = gold_coins[int(self.coin_index) % len(gold_coins)] if self.coin_state == 'gold' else silver_coins[int(self.coin_index)%len(silver_coins)]
        self.current_time = pygame.time.get_ticks()
    def render(self):
        #Clear the screen
        # self.screen.fill((220,170,120))
        self.screen.fill(SEA_COLOR)
        # self.screen.blit(self.background,(-100,-100))
        # self.clouds.draw(self.screen)
        # for bomb in self.bomb_tiles:
        #     pygame.draw.rect(self.screen,'Crimson',(bomb.rect.topleft-self.player.offset,bomb.rect.size))
        pygame.draw.rect(self.screen, '#eec39a',(0,0,self.screen_width,500))
        self.visible_sprites.render(self.player)
        self.screen.blit(self.coin_count, (70,95))
        self.screen.blit(self.display_coin,(30,90))
        self.screen.blit(health_bar, (30,30))
        for sprite in self.health:
            self.screen.blit(sprite.image,sprite.rect)
        # pygame.draw.rect(self.screen,'Crimson',(self.player.rect.topleft - self.player.offset,self.player.rect.size))
        # for bar in range(len(health_bars)):
        #     self.screen.blit(health_bars[bar],(bar*32+32,32))
        
        # for bar in range(len(bars)):
        #     self.screen.blit(bars[bar],(bar*32+62,56))
        # self.terrain.draw(self.screen)
        # self.enemies.draw(self.screen)
        
        debug(f"{len(self.health)}")
        # debug(f"{self.current_time - self.set_timer}",y = 50) 

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):

        while True:
            self.dt = self.clock.tick(self.FPS)
            self.handle_events()


            self.render()
            self.update()

            pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()
    
    
