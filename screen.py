import pygame
import math
import stockclass
pygame.init()
#INITIALIZED MODULES

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (248,248,255)

#COLOURS


win = pygame.display.set_mode((1200,800))
win.fill(WHITE)
test = stockclass.stock(win,(300,300,200,200),"Automax",BLACK,0,0)
test.createdatadisplay(GREEN)
test.createvisualdata(3)
pygame.display.update()
