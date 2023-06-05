import pygame, sys, pymunk
from settings import *
from level import *
from player import *

#Start
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
bg_img = pygame.image.load('graphics/Background/34893.jpg')
bg_img = pygame.transform.scale(bg_img,(screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

#Title on screen
font = pygame.font.Font("graphics/Fonts/Raleway-Black.ttf", 20)
text_title = font.render("Use coins to unlock characters", True, (0,0,0))

text_e = font.render("H = Elf, Attributes: Increased Speed  ", True, (0,0,0))

text_d = font.render("J = Dwarf, Attributes: Slide on walls ", True, (0,0,0))

text_s = font.render("K = Slime, Attributes: Bounce on surfaces. Can't jump ", True, (0,0,0))

text_w = font.render("L = Winged, Attributes: Double jump. Can float ", True, (0,0,0))



space = pymunk.Space()
space.gravity = (0.0, 900.0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_img,(0,0))

    space.step(1/50.0)

    level.run()

    screen.blit(text_title, (0,0))
    screen.blit(text_e, (0,30))
    screen.blit(text_d, (0,60))
    screen.blit(text_s, (0,90))
    screen.blit(text_w, (0,120))
    pygame.display.update()
    clock.tick(fps)
