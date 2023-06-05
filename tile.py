import pygame, csv, os

#green Tiles
class Tile_Green(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("#8FDB74")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

#Brown tiles
class Tile_Brown(pygame.sprite.Sprite):
     def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("#9b7653")
        self.rect = self.image.get_rect(topleft=pos)

     def update(self, x_shift):
         self.rect.x += x_shift

#White tiles
class Tile_White(pygame.sprite.Sprite):
     def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("#808080")
        self.rect = self.image.get_rect(topleft=pos)

     def update(self, x_shift):
         self.rect.x += x_shift


