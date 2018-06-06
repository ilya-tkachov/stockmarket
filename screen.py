import pygame
import math
import stockclass
import random
pygame.init()
#INITIALIZED MODULES

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (248,248,255)

#COLOURS


win = pygame.display.set_mode((1200,800))
ingame = False
inmenu = True
win.fill(WHITE)
#WINDOW AND WHILE LOOP VARIABLES

## Creates the visual stock data##

weeklyoutcome = [] #empty list that will be used for the stock data
for i in range(80): #Creates a list of 80 integers with values that range from -100 to 100
    i = random.randrange(-100,100)
    weeklyoutcome.append(i) #appends each i character to the list

##------------------------------##
while inmenu:
    win.fill(WHITE)
    buttontest =  stockclass.Button(win,(60,550,300,100))
    for i in range(3):
        buttontest.createbutton(440,550 - i*200)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            setposition = pygame.mouse.get_pos()
            print(setposition)
            buttontest.buttonclick(440,550,setposition)
            buttontest.buttonclick(440,350,setposition)
            buttontest.buttonclick(440,150,setposition)
##            if (buttontest.buttonclick(60,550,setposition)) == True :
##                inmenu = False
##                ingame = True
    pygame.display.update()

    
while ingame:

    test = stockclass.stock(win,(500,100,650,300),"Automax",BLACK,0,0)
    test.createdatadisplay(GREEN)
    test.createvisualdata(weeklyoutcome)
    test.createaxis()
    pygame.display.update()


    ##Creates the Buttons for the screen##
    buttontest =  stockclass.Button(win,(60,550,300,100))
    for i in range(3):
        buttontest.createbutton(60,550 - i*200)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            setposition = pygame.mouse.get_pos()
            print(setposition)
            buttontest.buttonclick(60,550,setposition)
            buttontest.buttonclick(60,350,setposition)
            buttontest.buttonclick(60,150,setposition)


        
            
    ##----------------------------------##


    pygame.display.update()
