import pygame
from pygame import image

class Collectible:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.sprite_sheet = image.load("images/coin.png")
        self.num_frames = 12
        self.frames = []
        self.collected = False

        for i in range(self.num_frames):
            frame_rect = pygame.Rect(i * self.width, 0, self.width, self.height)
            frame_image = self.sprite_sheet.subsurface(frame_rect)
            self.frames.append(frame_image)
        
        self.current_frame = 0
        self.last_frame_time = pygame.time.get_ticks()
        self.frame_interval = 100
    
    def get_sprite(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.frame_interval:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.last_frame_time = current_time
        
        return self.frames[self.current_frame]
    
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def collect(self):
        self.collected = True
    
