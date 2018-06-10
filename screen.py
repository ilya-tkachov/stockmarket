import pygame
import math
import stockclass
import random
pygame.init()
clock = pygame.time.Clock()
#INITIALIZED MODULES

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (248,248,255)
GREY = (193,205,205)
#COLOURS


win = pygame.display.set_mode((1200,800))
intermediate =  pygame.surface.Surface((1200,1500)) #screen for scrolling
game = True
instockwatch = False
inaccount = False
inmenu = True
scroll_y = 0
intermediate.fill(GREY)
mainlogo = pygame.image.load("logo.jpg")
#WINDOW AND WHILE LOOP VARIABLES

## Creates the visual stock data##
weeklyoutcome = [] #empty list that will be used for the stock data
for i in range(80): #Creates a list of 80 integers with values that range from -100 to 100
    i = random.randrange(-100,100)
    weeklyoutcome.append(i) #appends each i character to the list


##------------------------------##
while(game):
    while inmenu:
        win.fill(WHITE)
        buttontest =  stockclass.Button(win,(450,350,300,100),BLACK,"Start")
        win.blit(mainlogo,(380,150))

        buttontest.createbutton()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                buttontest.buttonclick(setposition)
                mainscreenbutton = (buttontest.buttonclick(setposition))
                if mainscreenbutton == True:
                    inmenu = False
                    inaccount = False
                    instockwatch = True
    ##          
        pygame.display.update()
    
    while instockwatch:
        win.fill(GREY)
        ##Creates the stock data for the screen##
        test = stockclass.stock(intermediate,(500,100,650,300),"NVDA",RED,0,0)
        test.createdatadisplay(BLACK)
        test.createvisualdata(weeklyoutcome)
        test.createaxis()
        ##------------------------------------------------------------------------##


        ##Creates the Buttons for the screen##
        Account =  stockclass.Button(intermediate,(20,0,270,70),BLACK,"Account",WHITE)
        Account.createbutton()
        Stockwatch = stockclass.Button(intermediate,(310,0,270,70),BLACK,"Stockwatch",WHITE)
        Stockwatch.createbutton()
        Dictionary = stockclass.Button(intermediate,(600,0,270,70),BLACK,"Dictionary",WHITE)
        Dictionary.createbutton()
        Exchange = stockclass.Button(intermediate,(890,0,270,70),BLACK,"Exchange",WHITE)
        Exchange.createbutton()
        ##--------------------------------------------------------------------------------------##
        

                
        ##-----------------------------------------------------------------##
        
        ##Events for the screen##
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                Account.buttonclick(setposition)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                Exchange.buttonclick(setposition)
                clickaccount = (Account.buttonclick(setposition))
                if clickaccount == True:
                    instockwatch = False
                    inmenu = False
                    inaccount = True
                if event.button == 4: #Events to scroll through the window
                    scroll_y = min(scroll_y + 15,0)
                if event.button == 5:
                    scroll_y = max(scroll_y - 15, -500)
        win.blit(intermediate,(0,scroll_y)) #Prevents the screen from flickering
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
        ##--------------------------------------------------------------------##

    while inaccount:
        ##Fills the screen##
        win.fill(GREY)
        intermediate.fill(GREY)
        ##--------------------##

        #Creates the main buttons located on top of the screen#
        Account =  stockclass.Button(win,(20,0,270,70),BLACK,"Account",WHITE)
        Account.createbutton()
        Stockwatch = stockclass.Button(win,(310,0,270,70),BLACK,"Stockwatch",WHITE)
        Stockwatch.createbutton()
        Dictionary = stockclass.Button(win,(600,0,270,70),BLACK,"Dictionary",WHITE)
        Dictionary.createbutton()
        Exchange = stockclass.Button(win,(890,0,270,70),BLACK,"Exchange",WHITE)
        Exchange.createbutton()
        ##-----------------------------------------------------##

        
        ##Manages the user bank information##
        userbank =  stockclass.Bankaccount(win,1000,0,400,500)
        userbank.initialfunds()
        userbank.addfunds(2.30,200)
        userbank.displaycurrentfunds()
        
        userbank.addfunds(200,2)
        userbank.changingfunds() #Prevents previous funds from being displayed
        userbank.displaycurrentfunds()
        
        userbank.addfunds(10,5)
        userbank.changingfunds()
        userbank.displaycurrentfunds() #3 tested entries of adding stocks
        
        #pygame.display.update()
        ##--------------------------------------------------------------------##

        ##Manage events for the game##
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                Account.buttonclick(setposition)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                Exchange.buttonclick(setposition)
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                if clickstockwatch == True:
                    inaccount = False
                    inmenu = False
                    instockwatch = True
        ##---------------------------##


        pygame.display.update()
