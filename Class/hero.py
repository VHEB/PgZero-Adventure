import pygame
from pygame import image

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.gravity = 5
        self.velocity_y = 0 
        self.velocity_x = 0 
        self.on_ground = False 

        self.width = 32  # Largura de cada frame
        self.height = 32  # Altura de cada frame
        self.sprite_sheet = image.load("images/idle.png")
        self.num_frames = 4
        
        self.frames = []
        for i in range(self.num_frames):
            frame_rect = pygame.Rect(i * self.width, 0, self.width, self.height)  
            frame_image = self.sprite_sheet.subsurface(frame_rect) 
            self.frames.append(frame_image)
        
        self.current_frame = 0  
        self.last_frame_time = pygame.time.get_ticks()  
        self.frame_interval = 200  

    def get_sprite(self):
        current_time = pygame.time.get_ticks()  
        if current_time - self.last_frame_time >= self.frame_interval:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.last_frame_time = current_time 
        
        return self.frames[self.current_frame]

    def update(self, platform_rect):

        self.x += self.velocity_x

        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.rect.colliderect(platform_rect):
            self.y = platform_rect.top - self.height  
            self.velocity_y = 0  
            self.on_ground = True  
        else:
            self.on_ground = False  

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
