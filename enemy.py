import pygame, random

#Coin sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphics/Coin/New Piskel (5).png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.centerx += x_shift
