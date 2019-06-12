import pygame
from pygame.locals import *
import sys
from random import *

# define constants
MINE_NUMB = 10
SCREEN_SIZE = (330,450)
SCREEN_COLOR = (150,150,150)
SQUARE_LENGTH = 30
SQUARE_SIZE = (SQUARE_LENGTH, SQUARE_LENGTH)
SQUARE_COLOR = (0,0,0)
LOCATION_NUMB1 = (30,30)
LOCATION_NUMB2 = (45,30)
LOCATION_RESTART = (140,50)


# input images
image_mine = pygame.image.load('mine.bmp')
image_numb = pygame.image.load('MineNumb.bmp')
image_restart = pygame.image.load('Restart.bmp')
name_mine = ["blank","flag","clickmine","wrongflag","mine",8,7,6,5,4,3,2,1,0]
name_numb = [9,8,7,6,5,4,3,2,1,0]
mineimgs = {}
for i in range(14): mineimgs[name_mine[i]] = image_mine.subsurface((0,i*30,30,30))
numbimgs = {}
for i in range(10): numbimgs[name_numb[i]] = image_numb.subsurface((0,i*25,15,25))


