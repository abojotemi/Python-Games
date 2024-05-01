import pygame, sys
from pygame import Vector2 as vector
from ball import Ball, BallMotion
from player import Player
from enemy import Enemy
from settings import *
from random import choice
class Game:
    def __init__(self):
        pygame.init()

#Screen settings
        self.screen_width = 1024
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong")

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()
        self.FPS = 60


        self.init_game()

    def init_game(self):
# Load game assets and initialize game state here
#		self.movement = pygame.Vector2(0,0)
        self.ball = Ball(self,(self.screen_width//2,self.screen_height//2))
        self.ball_group = pygame.sprite.GroupSingle(self.ball)
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player(self,(15,self.screen_height//2),self.player_group)
        self.enemy_group = pygame.sprite.GroupSingle()
        self.enemy = Enemy(self,(self.screen_width - 15,self.screen_height//2),self.enemy_group)
        self.ball_trail = pygame.sprite.GroupSingle()
        BallMotion(self.ball,self.ball_trail)
        self.background = pygame.transform.scale(pygame.image.load('assets/Board2.png'),(1024,640))
        self.start_time = pygame.time.get_ticks()
        self.count_down_font = pygame.font.SysFont('Jetbrains Mono',60)
        self.font = pygame.font.SysFont('Jetbrains Mono', 100)
        self.count_down = (3,2,1)
        self.score = 0
        self.e_score = 0
        self.dt = 0
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
        # Add event handling code here
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.direction.x = 1
                if event.key == pygame.K_DOWN:
                    self.player.direction.y = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.direction.x = 0
                if event.key == pygame.K_DOWN:
                    self.player.direction.y = 0

    def update(self):
        #Update game logic here
        if not  0 < self.ball.rect.x < self.screen_width:
                if self.ball.rect.x <= 0:
                    self.e_score += 1
                if self.ball.rect.x >= self.screen_width:
                    self.score += 1
                self.ball.rect.center = (self.screen_width//2, self.screen_height//2)
                self.ball.direction = vector(choice([-1,1]),choice([-1,1]))
                self.player_group.empty()
                self.player = Player(self,(15,self.screen_height//2),self.player_group)
                self.enemy_group.empty()
                self.enemy = Enemy(self,(self.screen_width - 15,self.screen_height//2),self.enemy_group)
                
                
                self.ball_trail.empty()
                BallMotion(self.ball,self.ball_trail)
                
                self.start_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > 3000:
            self.ball_group.update(self.player,self.enemy)
            self.player_group.update()
            self.enemy_group.update(self.ball)
            self.ball_trail.update()
            

    def render(self):
        #Clear the screen
        self.screen.fill((220,170,120))
        self.screen.blit(self.background, (0,0))
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.player_score = self.font.render(f"{self.score}",True,'White')
        # self.player_score.set_alpha(100)
        self.player_rect = self.player_score.get_rect(center = (self.screen_width//4,self.screen_height//2) )
        self.enemy_score = self.font.render(f"{self.e_score}",True,'White')
        # self.enemy_score.set_alpha(100)
        self.enemy_rect = self.enemy_score.get_rect(center = (self.screen_width*3//4,self.screen_height//2) )        
        
        if self.current_time - self.start_time > 3000:
            self.ball_trail.draw(self.screen)
            self.player_score.set_alpha(100)
            self.enemy_score.set_alpha(100)
        else:
            self.player_score.set_alpha(255)
            self.enemy_score.set_alpha(255)
        self.screen.blit(self.player_score,self.player_rect)
        self.screen.blit(self.enemy_score,self.enemy_rect)
        self.ball_group.draw(self.screen)
        if self.current_time - self.start_time < 3000:
            self.countdown = self.count_down_font.render(f"{self.count_down[int((self.current_time - self.start_time)/1000)]}", True,'White')
            self.countdown_rect = self.countdown.get_rect(center = (self.screen_width//2,30))
            self.screen.blit(self.countdown, self.countdown_rect)
        # debug(self.dt)
    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):

        while True:
            self.handle_events()
            self.current_time = pygame.time.get_ticks()
            self.update()

            self.render()

            self.dt = self.clock.tick(self.FPS)
            pygame.display.update()
if __name__ == '__main__':
    game = Game()
    game.run()
    
    
    
