import pygame
from settings import *
from support import *
from level import *
from guizero import *

#Class for making Character
class Player_Elemental(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        #Graphics
        self.animations = {}
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.10
        self.character_status = "elemental"
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 20
        self.jump_speed = -16
        self.jump_counter = 0
        self.counter = 0
        self.float_speed = 4
        self.in_air = False

        #Sounds
        self.jump_sound = pygame.mixer.Sound("sound/effects/cartoon-jump-6462.mp3")
        self.run_sound = pygame.mixer.Sound("sound/effects/running-1-6846.mp3")
        self.status = "idle"

    #Animation
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    #Assets for animation
    def import_character_assets(self):
        character_path = "graphics/player_elemental/"
        self.animations = {"idle":[], "run":[], "jump":[], "run_left": [], "jump_left": [], "idle_dwarf":[], "jump_dwarf":[]
                           , "jump_2":[], "idle_slime":[], "run_left_slime":[], "fall_slime":[], "jump_slime":[], "on_wall":[]
                           , "idle_winged":[], "jump_winged":[], "run_right_winged":[], "run_left_winged":[], "run_right_slime":[],
                           "run_right_dwarf":[], "run_left_dwarf":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    #Coding the inputs given by player
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.character_status == "elemental":
                self.direction.x = 1.5
            elif self.character_status == "dwarf" or self.character_status == "winged":
                self.direction.x = 1
            elif self.character_status == "still" or self.character_status == "slime":
                self.direction.x = 0.7
        elif keys[pygame.K_LEFT]:
            if self.character_status == "elemental":
                self.direction.x = -1.5
            elif self.character_status == "dwarf" or self.character_status == "winged":
                self.direction.x = -1
            elif self.character_status == "still" or self.character_status == "slime":
                self.direction.x = -0.7
        else:
            self.direction.x = 0
        if keys[pygame.K_DOWN]:
            self.slide()
        if keys[pygame.K_SPACE]:
            self.jump()
        elif keys[pygame.K_j]:
            if self.counter > 0:
                self.character_status = "dwarf"
                self.status = "idle_dwarf"
        elif keys[pygame.K_h]:
            self.character_status = "elemental"
            self.status = "idle"
        elif keys[pygame.K_k]:
            if self.counter > 1:
                if self.direction.y > 0 or self.direction.y < 0:
                    if self.character_status != "still":
                        self.character_status = "slime"
                        self.status = "idle_slime"
                elif self.direction.y == 0:
                    self.character_status = "still"
                    self.status = "idle_slime"
        elif keys[pygame.K_l]:
            if self.counter > 2:
                self.character_status = "winged"
                self.status = "idle_winged"

    #Changing status
    def get_status(self):
        if self.direction.y == 0:
            if self.direction.x == 0:
                if self.character_status == "elemental":
                    self.status = "idle"
                elif self.character_status == "dwarf":
                    self.status = "idle_dwarf"
                elif self.character_status == "slime":
                    self.status = "idle_slime"
                elif self.character_status == "still":
                    self.status = "idle_slime"
                elif self.character_status == "winged":
                    self.status = "idle_winged"
            elif self.direction.x > 0:
                if self.character_status == "elemental":
                    self.status = "run"
                elif self.character_status == "dwarf":
                    self.status = "run_right_dwarf"
                elif self.character_status == "winged":
                    self.status = "run_right_winged"
                elif self.character_status == "still":
                    self.status = "run_right_slime"
            elif self.direction.x < 0:
                if self.character_status == "elemental":
                    self.status = "run_left"
                elif self.character_status == "dwarf":
                    self.status = "run_left_dwarf"
                elif self.character_status == "still":
                    self.status = "run_left_slime"
                elif self.character_status == "winged":
                    self.status = "run_left_winged"
        if self.direction.y > 0 and self.character_status == "slime":
            self.status = "fall_slime"
        elif self.direction.y < 0 and self.character_status == "slime":
            self.status = "jump_slime"

        if self.direction.y >= 100:
            self.kill()


    #Function for jumping
    def jump(self):
        #Only if character is Elemental
        if self.character_status == "elemental":
            if self.status != "jump":
                self.status = "jump"
                self.direction.y = self.jump_speed
                pygame.mixer.Sound.play(self.jump_sound)
        if self.character_status == "dwarf":
            if self.status != "jump_dwarf":
                self.status = "jump_dwarf"
                self.direction.y = self.jump_speed
                pygame.mixer.Sound.play(self.jump_sound)
        #Only if character is dwarf
        if self.character_status == "winged":
            if self.status != "jump_winged" and self.status != "jump_2":
                self.status = "jump_winged"
                self.direction.y = self.jump_speed
                pygame.mixer.Sound.play(self.jump_sound)
            elif self.direction.y > 0 and self.status != "jump_2" and self.character_status == "winged":
                self.status = "jump_2"
                self.direction.y = self.jump_speed + 3
                pygame.mixer.Sound.play(self.jump_sound)

    def slide(self):
        pass

    #moving horizontally
    def horizontal_movement_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                    if self.character_status == "dwarf":
                        self.direction.y = 0
                        self.status = "on_wall"
                        self.apply_gravity()
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left
                    if self.character_status == "dwarf":
                        self.direction.y = 0
                        self.status = "on_wall"
                        self.apply_gravity()
    #Moving Vertically
    def vertical_movement_collision(self, tiles):
        self.apply_gravity()
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                    if self.character_status == "slime":
                        self.direction.y = -self.direction.y
                        self.character_status = "still"
                    else:
                        self.direction.y = 0
                        if self.character_status != "still":
                            self.status = "idle"

    #Applying Gravity
    def apply_gravity(self):
        #Different gravity for winged character
        if self.character_status != "winged":
            self.direction.y += gravity
            self.rect.y += self.direction.y
        if self.character_status == "winged" and self.direction.y <= 0:
            self.direction.y += gravity
            self.rect.y += self.direction.y
            self.speed = 10
        elif self.character_status == "winged" and self.direction.y > 0:
            self.direction.y += gravity - 0.7
            self.rect.y += self.direction.y
            self.speed = 10
        else:
            self.speed = 20





    #Updating the commands
    def update(self, tiles):
        self.get_input()
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)
        self.get_status()
        self.animate()

