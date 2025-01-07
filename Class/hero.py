import pygame
from pygame import image

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.gravity = 2
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

    def update(self, platforms):
        # Atualiza a posição horizontal
        self.x += self.velocity_x

        # Aplica gravidade
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Assume que o herói não está no chão
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform):
                # Colisão por cima da plataforma
                if self.velocity_y > 0 and self.y + self.height <= platform.top + self.velocity_y:
                    self.y = platform.top - self.height
                    self.velocity_y = 0
                    self.on_ground = True
                # Colisão por baixo da plataforma (se necessário)
                elif self.velocity_y < 0 and self.y >= platform.bottom - self.velocity_y:
                    self.y = platform.bottom
                    self.velocity_y = 0
                # Colisão lateral (esquerda ou direita)
                elif self.x + self.width > platform.left and self.x < platform.right:
                    if self.velocity_x > 0:  # Movendo para a direita
                        self.x = platform.left - self.width
                    elif self.velocity_x < 0:  # Movendo para a esquerda
                        self.x = platform.right
                    self.velocity_x = 0

        # Verifica se o herói está fora do limite inferior da tela (queda livre)
        if self.y > 600 - self.height:
            self.y = 600 - self.height
            self.velocity_y = 0
            self.on_ground = True
        
        # Impedir o herói de atravessar as bordas da tela
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > 800:  # Largura da tela definida em main.py
            self.x = 800 - self.width

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
