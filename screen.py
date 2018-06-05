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

## Creates the visual stock data##
test = stockclass.stock(win,(300,200,650,300),"Automax",BLACK,0,0)
test.createdatadisplay(GREEN)
test.createvisualdata(3)
test.createaxis()
##------------------------------##

##Creates the Buttons for the screen##
buttontest =  stockclass.Button(win,(60,100,200,200))
buttontest.createbutton()

pygame.display.update()
