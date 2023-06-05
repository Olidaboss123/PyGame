import pygame, sys
from settings import *
from tile import *
from player import *
from enemy import *

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)
        self.counter = 0

        #Background music
        self.world_shift = 0
        pygame.mixer.music.load("sound/music/background_song.mp3")
        pygame.mixer.music.play(-1)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                #Different coloured tiles put on map
                if cell == "x":
                    tile = Tile_Green((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "y":
                    tile_brown = Tile_Brown((x, y), tile_size)
                    self.tiles.add(tile_brown)
                elif cell == "w":
                    tile_white = Tile_White((x,y), tile_size)
                    self.tiles.add(tile_white)
                elif cell == "p":
                    player_sprite = Player_Elemental((x,y))
                    self.player.add(player_sprite)
                elif cell == "e":
                    item_sprite = Enemy((x,y))
                    self.enemies.add(item_sprite)

    #Scrolling
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x > screen_width - (screen_width/3) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        elif player_x < screen_width/3 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8


    def run(self):
        #Create all sprites and blocks
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.player.update(self.tiles)
        self.player.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.enemies.update(self.world_shift)

        # Detect collisions between player and items
        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.enemies, True)
        if len(collided_with) == 1:
            self.player.sprite.counter += 1
        elif len(collided_with) == 2:
            self.player.sprite.counter += 1
        elif len(collided_with) == 3:
            self.player.sprite.counter += 1
        elif len(collided_with) == 4:
            self.player.sprite.counter += 1


