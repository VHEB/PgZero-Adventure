import pygame
import pgzrun
from pygame import image

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 5
        self.speed = 2
        self.velocity_y = 0
        self.velocity_x = 0
        self.on_ground = False
        
        self.image = image.load("images/enemy.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    def update(self, platform_rect):
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        self.velocity_y += self.gravity
        
        if self.rect.colliderect(platform_rect):
            self.y = platform_rect.top - self.height
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)