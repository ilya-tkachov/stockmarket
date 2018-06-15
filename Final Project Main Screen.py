import pygame
import math
import stockclass
import random
from class_stockdata import *
from class_getindex import *
import time
import os  

os.environ['SDL_VIDEO_CENTERED'] = '1'

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


win = pygame.display.set_mode((1200,800),pygame.NOFRAME)
intermediate =  pygame.surface.Surface((1200,1500)) #screen for scrolling
game = True
instockwatch = False
inaccount = False
indictionary = False
inexchange = False
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




#--world map--#
maps = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\map.png")),(800,400))
asia = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\asia_isolate.png")),(800,400))
north_america = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\north_america_isolate.png")),(800,400))
europe = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\europe_isolate.png")),(800,400))

map_img = [maps,asia,europe,north_america]
ver = "v1-ri-ini"
#----------------------------------------------#
class top_bar(object):
    def __init__(self,win,position,color,version,time,market=False):
        self.win = win
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.w = position[2]
        self.h = position[3]
        self.color = color
        self.version = version
        self.time = time
        self.font = pygame.font.SysFont("arialrounded", self.h-2)

    def update(self,time,market):
        pygame.draw.rect(self.win,self.color,(self.x,self.y,self.w,self.h))
        version_ui = self.font.render(self.version,0,(0,0,0))
        time_ui = self.font.render(time,0,(0,0,0))
        if market == True:
            market_ui = self.font.render("OPEN",0,(0,215,65))
        else:
            market_ui = self.font.render("CLOSED",0,(220,0,0))
        self.win.blit(version_ui,(0,0))
        self.win.blit(time_ui,(75,0))
        self.win.blit(market_ui,(175,0))






##------------------------------##


##------------------------------##
event = pygame.event.get()
menu_bar = top_bar(win,[0,0,1200,15],(186,186,186),ver,"HH:MM:APM")
for x in event:
    if event is pygame.QUIT:
        pygame.quit()
        #raise SystemExit
    else:
        menu_bar.update(str(time.strftime("%I:%M%p [%S]")),check_market_time())
        pygame.display.update()

    #raise SystemExit
        
while(game): #Main while loop to keep the game running 

 

    while inmenu: #Menu screen for the game 
        win.fill(WHITE) #Fills the window with a chosen color
        buttontest =  stockclass.Button(win,(450,350,300,100),BLACK,"Start") #Calls the class to create the button and its characteristics
        win.blit(mainlogo,(390,150)) #Blits the logo jpeg onto the screen on the given coordinates

        buttontest.createbutton() #Displays the button and essentially creates its existence for the screen




        pygame.draw.rect(win,(22,22,22),(200,600,800,400)) #Black rectangle used for the map
        for i in map_img: #Map coordinates
            win.blit(i,(200,600))


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos() #Gets the mouse position coordinates
                print(setposition)
                buttontest.buttonclick(setposition) #Checks if the "buttontest" button has been clicked
                mainscreenbutton = (buttontest.buttonclick(setposition)) #Sets a variable equal to the button click will return True if Clicked False for anything else
                if mainscreenbutton == True: #If the button is clicked set all while loops to false except for the stockwatch loop
                    inmenu = False
                    inaccount = False
                    indictionary = False
                    inexchange = False
                    instockwatch = True
    ##          
        pygame.display.update() #Updates display

        
    
    while instockwatch: #Main while loop for the stockwatch section of the game
        win.fill(GREY) #Fills the screen with a certain color

        
        ##Creates the stock data for the screen##
        test = stockclass.stock(intermediate,(500,100,650,300),"NVDA",RED,0,0) 
        test.createdatadisplay(BLACK) #Creates the rectangle background
        test.createvisualdata(weeklyoutcome) #Displays the line *weekly outcome is the list of values (refer to top of the code)*
        test.createaxis() #Creates the x and y axis
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
        for i in range (6): #Creates 6 test buttons using a for loop (Not really needed)
            testbutton = stockclass.Button(intermediate,(20,300 + i *100,270,70),BLACK,"test",WHITE)
            testbutton.createbutton()

                
        ##-----------------------------------------------------------------##

        ## Table display of stock info##

        nvdatable = stockclass.Stocktable(intermediate,"NAME", "VALUE", "NETCHANGE", "%CHANGE", "1MONTH", "1YEAR", "TIME")
        nvdatable.createtable(500,550,650,200,WHITE) #Creates the rectangle for the table
        nvdatable.addinfo("NVDA",str(3.50),str(10.20),str(30.00),str(2),str(2.2),"2:32PM",500,550,650,200) #Adds info into the table (Repeat x,y,width,height when calling for each method)


        ##------------------------------------------------------------------##
        
        ##Events for the screen##
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                Account.buttonclick(setposition) #Sets up a button click check for each section of the application (Account, Stockwatch, Dictionary and exchange)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                Exchange.buttonclick(setposition)
                clickaccount = (Account.buttonclick(setposition)) #Sets variables equal to the returned value (makes it easier to do checks)
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                clickdictionary = (Dictionary.buttonclick(setposition))
                clickexchange = (Exchange.buttonclick(setposition))
                if clickaccount == True: #If the account button was clicked access the account while loop only
                    instockwatch = False
                    inmenu = False
                    indictionary = False
                    inexchange = False
                    inaccount = True
                elif clickstockwatch == True: #If the stockwatch button was clicked access the stockwatch while loop only
                    inmenu = False
                    inaccount = False
                    indictionary = False
                    inexchange = False
                    instockwatch = True
                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
                    inmenu = False
                    inaccount = False
                    inexchange = False
                    instockwatch = False
                    indictionary = True
                elif clickexchange == True: #If the exchange button was clicked access the exchange while loop only
                    instockwatch = False
                    inmenu = False
                    inaccount = False
                    indictionary = False
                    inexchange= True
                    

##                    
                if event.button == 4: #Events to scroll through the window
                    scroll_y = min(scroll_y + 15,0)
                if event.button == 5:
                    scroll_y = max(scroll_y - 15, -500)
        win.blit(intermediate,(0,scroll_y)) #Prevents the screen from flickering
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
        ##--------------------------------------------------------------------##





    while inaccount: #Main while loop for the account section of the game

        
        ##Fills the screen##
        win.fill(GREY)
        intermediate.fill(GREY) #Intermediate screen replaces the main window and is used for scrolling
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
        userbank.addfunds(2.30,200) #adds funds (Sharevalue, amount of shares)
        userbank.displaycurrentfunds()
        
        userbank.addfunds(200,2)
        userbank.changingfunds() #Prevents previous funds from being displayed (Blits a rectangle with same screen color over previous data at the same spot)
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
                Account.buttonclick(setposition) #Sets up buttonclick functionality for the 4 main buttons (account,stockwatch,dictionary,exchange)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                Exchange.buttonclick(setposition)
                clickaccount = (Account.buttonclick(setposition)) #Sets variables equal to their return value True or False
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                clickdictionary = (Dictionary.buttonclick(setposition))
                clickexchange = (Exchange.buttonclick(setposition))
                if clickaccount == True: #If the account button was clicked access the account while loop only
                    instockwatch = False
                    inmenu = False
                    indictionary = False
                    inexchange = False
                    inaccount = True
                elif clickstockwatch == True:#If the stockwatch button was clicked access the stockwatch while loop only
                    inmenu = False
                    inaccount = False
                    indictionary = False
                    inexchange = False
                    instockwatch = True
                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
                    inmenu = False
                    inaccount = False
                    inexchange = False
                    instockwatch = False
                    indictionary = True
                elif clickexchange == True:#If the exchange button was clicked access the exchange while loop only
                    inaccount = False
                    inmenu = False
                    instockwatch = False
                    indictionary = False
                    inexchange = True

                
        pygame.display.update()
        ##---------------------------##




        

    while indictionary:
        win.fill(GREY)
        intermediate.fill(GREY)
        
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
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                Account.buttonclick(setposition)#Sets up buttonclick functionality for the 4 main buttons (account,stockwatch,dictionary,exchange)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                Exchange.buttonclick(setposition)
                clickaccount = (Account.buttonclick(setposition))#Sets variables equal to their return value True or False
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                clickdictionary = (Dictionary.buttonclick(setposition))
                clickexchange = (Exchange.buttonclick(setposition))
                if clickaccount == True:#If the account button was clicked access the account while loop only
                    instockwatch = False
                    inmenu = False
                    indictionary = False
                    inexchange = False
                    inaccount = True
                elif clickstockwatch == True:#If the stockwatch button was clicked access the stockwatch while loop only
                    inmenu = False
                    inaccount = False
                    indictionary = False
                    inexchange = False
                    instockwatch = True
                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
                    inmenu = False
                    inaccount = False
                    inexchange = False
                    instockwatch = False
                    indictionary = True
                elif clickexchange == True:#If the exchange button was clicked access the exchange while loop only
                    inaccount = False
                    inmenu = False
                    instockwatch = False
                    indictionary = False
                    inexchange = True
        
        
        pygame.display.update() #Update display

    while inexchange:
        win.fill(GREY)
        intermediate.fill(GREY)
        
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
            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                Account.buttonclick(setposition)#Sets up buttonclick functionality for the 4 main buttons (account,stockwatch,dictionary,exchange)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                Exchange.buttonclick(setposition)
                clickaccount = (Account.buttonclick(setposition))#Sets variables equal to their return value True or False
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                clickdictionary = (Dictionary.buttonclick(setposition))
                clickexchange = (Exchange.buttonclick(setposition))
                if clickaccount == True:#If the account button was clicked access the account while loop only
                    instockwatch = False
                    inmenu = False
                    indictionary = False
                    inexchange = False
                    inaccount = True
                elif clickstockwatch == True:#If the stockwatch button was clicked access the stockwatch while loop only
                    inmenu = False
                    inaccount = False
                    indictionary = False
                    inexchange = False
                    instockwatch = True
                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
                    inmenu = False
                    inaccount = False
                    inexchange = False
                    instockwatch = False
                    indictionary = True
                elif clickexchange == True:#If the exchange button was clicked access the exchange while loop only
                    inaccount = False
                    inmenu = False
                    instockwatch = False
                    indictionary = False
                    inexchange = True
                
                
        pygame.display.update()
