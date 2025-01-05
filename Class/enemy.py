import pygame
from pygame import image

class Enemy:
    def __init__(self, x, y, left_limit, right_limit):
        self.x = x
        self.y = y
        self.gravity = 5
        self.speed = 2
        self.velocity_y = 0
        self.velocity_x = self.speed
        self.on_ground = False
        self.left_limit = left_limit
        self.right_limit = right_limit

        self.image = image.load("images/enemy.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, platform_rect):
        self.x += self.velocity_x
        if self.x <= self.left_limit or self.x + self.width >= self.right_limit:
            self.velocity_x *= -1  # Inverte a direção

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
