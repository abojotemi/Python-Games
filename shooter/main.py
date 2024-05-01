import pygame, sys
from pygame import Vector2 as vector
from settings import *
from player import Player
from bullets import Bullet
from enemy import Enemy
from random import randint
from health import *
from math import sin
class Game:
    def __init__(self):
        pygame.init()

#Screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Your Game Title")

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.font = pygame.font.SysFont("Jetbrains Mono", 50)
        self.score_font = pygame.font.SysFont("Jetbrains Mono", 150)

        self.init_game()
        self.current_time = 0

    def init_game(self):
# Load game assets and initialize game state here
#		self.movement = pygame.Vector2(0,0)
        self.player_group = pygame.sprite.Group()
        self.player = Player(self,self.player_group)
        self.bullets = pygame.sprite.Group()
        self.start_time = 0
        self.OPP_COUNTER = pygame.USEREVENT
        self.enemy = pygame.sprite.Group()
        self.score = 0
        self.health = pygame.sprite.Group()
        self.game_on = False
        self.start = False
        self.heart_time = 0
        self.heart = pygame.sprite.Group()
        pygame.time.set_timer(self.OPP_COUNTER,1000)
        for i in range(10):
            Health(self,(i * self.screen_width/10 + 1,self.screen_height),self.health,i+1)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
        # Add event handling code here
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.direction.x = 1
                if event.key == pygame.K_RIGHT:
                    self.player.direction.y = 1
                if event.key == pygame.K_SPACE:
                    if not self.game_on and not self.start:
                        self.game_on = True
                        self.start = True
                    if self.game_on:
                        if self.current_time - self.start_time > 600:
                            bullet1 =Bullet(self,(self.player.rect.midleft[0] + 20,self.player.rect.midleft[1]-30),self.bullets)
                            bullet2 = Bullet(self,(self.player.rect.midright[0] - 20,self.player.rect.midright[1]-30),self.bullets)
                            bullet1.partner = bullet2
                            bullet2.partner = bullet1
                            self.start_time = pygame.time.get_ticks()
                        if self.current_time - self.heart_time > 20000 and len(self.health) < 10:
                            Heart(self,(randint(100,850),-randint(100,300)),self.heart)
                            self.heart_time = pygame.time.get_ticks()
                    elif not self.game_on and self.start:
                        self.player_group.empty()
                        self.player = Player(self,self.player_group)
                        self.enemy.empty()
                        self.bullets.empty()
                        self.score = 0
                        self.health.empty()
                        for i in range(10):
                            Health(self,(i * self.screen_width/10 + 1,self.screen_height),self.health,i+1)
                        self.game_on = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.direction.x = 0
                if event.key == pygame.K_RIGHT:
                    self.player.direction.y = 0
            if event.type == self.OPP_COUNTER:
                Enemy(self,(randint(100,850),-randint(100,300)),self.enemy)

    def update(self):
        #Update game logic here
        if self.game_on:
            self.player.update(self.health, self.enemy)
            self.bullets.update(self.enemy)
            self.enemy.update()
            self.score_text = self.score_font.render(f"{self.score}",True, "White")
            self.score_text.set_alpha(100)
            self.score_text_rect = self.score_text.get_rect(center = (self.screen_width//2,self.screen_height//2))
            self.heart.update(self.player,self.health)
            self.health.update()
    def render(self):
        #Clear the screen
        self.screen.fill((20,30,30))
        if not self.game_on and not self.start:
            self.text = self.font.render(f"Press Space to Start",True,"White")
            self.text_rect = self.text.get_rect(center =(self.screen_width//2, self.screen_height//2) )
            self.screen.blit(self.text,self.text_rect)
        if not self.game_on and self.start:
            self.text2 = self.font.render(f"      Game Over\nYour last score was {self.score}",True,"White")
            self.text2_rect = self.text2.get_rect(center =(self.screen_width//2, self.screen_height//3) )            
            self.screen.blit(self.text2,self.text2_rect)
            self.text1 = self.font.render(f"Press Space to Start",True,"White")
            self.text1_rect = self.text1.get_rect(center =(self.screen_width//2, self.screen_height*2//3) )
            self.screen.blit(self.text1,self.text1_rect)
        if self.game_on:
            self.screen.blit(self.score_text,self.score_text_rect)
            self.health.draw(self.screen)
            self.heart.draw(self.screen)
            self.bullets.draw(self.screen)
            self.enemy.draw(self.screen)
            self.player_group.draw(self.screen)
            # debug(sin(int(self.current_time)//20))
            # debug(sin(int(self.current_time))*20,y = 50)

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):

        while True:
            if self.game_on:
                self.current_time = pygame.time.get_ticks()
            self.handle_events()


            self.update()
            self.render()

            self.clock.tick(self.FPS)
            pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()