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
intermediate =  pygame.surface.Surface((1200,3000)) #screen for scrolling
game = True
instockwatch = False
inaccount = False
indictionary = False
inexchange = False
inmenu = True
scroll_y = 0
intermediate.fill(GREY)
mainlogo = pygame.image.load("logo.jpg")
clickedname = None
stockwatchbuttons =[]
chosenstock = []
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

    def bar_update(self,time,market):
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



temp_time = time.time()
print("Select Continent")
print(continets)
c = input(":")
print("Select Market")
print(select_market(c))
smbls = select_index(select_market(c),input(":"))

f_nasdaq()
m = market(smbls)







##------------------------------##


##------------------------------##
event = pygame.event.get()
menu_bar = top_bar(win,[0,0,1200,15],(186,186,186),ver,"HH:MM:APM")



def update():
    temp_time = time.time()
    event = pygame.event.get()
    for x in event:
        if event is pygame.QUIT:
            pygame.quit()
            raise SystemExit
    if float(time.time()) >= float(temp_time)+62: #Change back to 2 seconds (updates)
        update_realtime_prices(m)
        #print("...Updated Prices...")
        temp_time = time.time()
    menu_bar.bar_update(str(time.strftime("%I:%M%p [%S]")),check_market_time())
    pygame.display.update()
    
    #raise SystemExit

def visualdataclick(name,price):
    test = stockclass.stock(win,(500,100,650,300),str(name),RED,0,0) 
    test.createdatadisplay(BLACK) #Creates the rectangle background
    test.createvisualdata(price) #Displays the line *weekly outcome is the list of values (refer to top of the code)*
    test.createaxis() #Creates the x and y axis

def datatable(name,value,netchange,time):
    nvdatable = stockclass.Stocktable(win,"NAME", "VALUE", "NETCHANGE", "", "", "", "TIME")
    nvdatable.createtable(500,550,650,200,WHITE) #Creates the rectangle for the table
    nvdatable.addinfo(str(name),str(value),str(netchange),"","","",str(time),500,550,650,200) #Adds info into the table (Repeat x,y,width,height when calling for each method)

def dictionarytable(name,info):
    extratable = stockclass.Stocktable(win,"Name","","Information","","","","")
    extratable.createtable(500,100,650,200,BLACK)
    extratable.addinfo(str(name),"",str(info),"","","","",500,100,650,200)
while(game): #Main while loop to keep the game running 

 

    while inmenu: #Menu screen for the game
        win.fill(WHITE) #Fills the window with a chosen color
        buttontest =  stockclass.Button(win,(450,550,300,100),BLACK,"Start") #Calls the class to create the button and its characteristics
        win.blit(mainlogo,(390,400)) #Blits the logo jpeg onto the screen on the given coordinates

        buttontest.createbutton() #Displays the button and essentially creates its existence for the screen




        pygame.draw.rect(win,(22,22,22),(190,0,800,400)) #Black rectangle used for the map
        for i in map_img: #Map coordinates
            win.blit(i,(190,0))


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
        update()
        pygame.display.update() #Updates display

        
    
    while instockwatch: #Main while loop for the stockwatch section of the game
        win.fill(GREY) #Fills the screen with a certain color





        
        ##Creates the stock data for the screen##

        ##------------------------------------------------------------------------##

        Stockwatch = stockclass.Button(win,(310,0,270,70),BLACK,"Stockwatch",WHITE)
        Stockwatch.createbutton()
        Dictionary = stockclass.Button(win,(600,0,270,70),BLACK,"Dictionary",WHITE)
        Dictionary.createbutton()
        
        ##--------------------------------------------------------------------------------------##
        for z in range(len(m.data)):
            stockwatchbuttons.append(("Button" + str("i"*z)))
        for q in range(len(m.data)):
            chosenstock.append(("Stock"+str("i"*q)))
        for i in range (len(m.data)): 
            stockwatchbuttons[i] = stockclass.Button(win,(20,100 + i *100,270,70),BLACK,m.data[i].ticker,WHITE,(0,0,0),1,100)
            stockwatchbuttons[i].createbutton()

        ##-----------------------------------------------------------------##




        ##------------------------------------------------------------------##
        ##Events for the screen##
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                clickdictionary = (Dictionary.buttonclick(setposition))
                for q in range(len(m.data)):
                    (stockwatchbuttons[q]).buttonclick(setposition) #Checks for button click on each stock
                    chosenstock[q] = (stockwatchbuttons[q]).buttonclick(setposition) #sets a unique variable equal to the button click
                    stockwatchbuttons[q].getstockname(setposition) #Gets the name of the stock
            
                if clickstockwatch == True: #If the stockwatch button was clicked access the stockwatch while loop only
                    inmenu = False
                    indictionary = False
                    instockwatch = True
                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
                    inmenu = False
                    instockwatch = False
                    indictionary = True

        for i in range(len(m.data)):
            if chosenstock[i] == True: #If the button is clicked
                stockname = (stockwatchbuttons[i].getstockname(setposition))
                g = []
                for a in m.fetch(stockname[0]).info:
                    g.append(float(a[0]))
                print(g)
                visualdataclick(stockname[0],g)
                datatable(stockname[0],g[0],0,m.fetch(stockname[0]).time())


                

        update()
        pygame.display.update()

        ##--------------------------------------------------------------------##



    while indictionary:
        win.fill(GREY)
        intermediate.fill(GREY)
        

        Stockwatch = stockclass.Button(win,(310,0,270,70),BLACK,"Stockwatch",WHITE)
        Stockwatch.createbutton()
        Dictionary = stockclass.Button(win,(600,0,270,70),BLACK,"Dictionary",WHITE)
        Dictionary.createbutton()

        ##-----------------------------------------------------##
        for z in range(len(m.data)):
            stockwatchbuttons.append(("Button" + str("i"*z)))
        for q in range(len(m.data)):
            chosenstock.append(("Stock"+str("i"*q)))
        for i in range (len(m.data)): 
            stockwatchbuttons[i] = stockclass.Button(win,(20,100 + i *100,270,70),WHITE,m.data[i].ticker,RED,(0,0,0),1,100)
            stockwatchbuttons[i].createbutton()


        ##-----------------------------------------------------##


        ##-----------------------------------------------------##
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                setposition = pygame.mouse.get_pos()
                print(setposition)
                Stockwatch.buttonclick(setposition)
                Dictionary.buttonclick(setposition)
                clickstockwatch = (Stockwatch.buttonclick(setposition))
                clickdictionary = (Dictionary.buttonclick(setposition))
                for q in range(len(m.data)):
                    (stockwatchbuttons[q]).buttonclick(setposition) #Checks for button click on each stock
                    chosenstock[q] = (stockwatchbuttons[q]).buttonclick(setposition) #sets a unique variable equal to the button click
                    stockwatchbuttons[q].getstockname(setposition) #Gets the name of the stock
                if clickstockwatch == True:#If the stockwatch button was clicked access the stockwatch while loop only
                    inmenu = False
                    indictionary = False
                    instockwatch = True
                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
                    inmenu = False
                    instockwatch = False
                    indictionary = True
        for i in range(len(m.data)):
            if chosenstock[i] == True: #If the button is clicked
                stockname = (stockwatchbuttons[i].getstockname(setposition))
                g = []
                for a in m.fetch(stockname[0]).info:
                    g.append(float(a[0]))
                    dictionarytable(stockname[0],"Info Goes Here")

        
        update()
        pygame.display.update() #Update display
raise SystemExit







## Unfinished Content :( ---------------------------------------------------------------------------------------##
##--------------------------------------------------------------------------------------------------------------##
##    while inexchange:
##        win.fill(GREY)
##        intermediate.fill(GREY)
##        
##                    #Creates the main buttons located on top of the screen#
##        Account =  stockclass.Button(win,(20,0,270,70),BLACK,"Account",WHITE)
##        Account.createbutton()
##        Stockwatch = stockclass.Button(win,(310,0,270,70),BLACK,"Stockwatch",WHITE)
##        Stockwatch.createbutton()
##        Dictionary = stockclass.Button(win,(600,0,270,70),BLACK,"Dictionary",WHITE)
##        Dictionary.createbutton()
##        Exchange = stockclass.Button(win,(890,0,270,70),BLACK,"Exchange",WHITE)
##        Exchange.createbutton()
##        ##-----------------------------------------------------##
##            
##        for event in pygame.event.get():
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                setposition = pygame.mouse.get_pos()
##                print(setposition)
##                Account.buttonclick(setposition)#Sets up buttonclick functionality for the 4 main buttons (account,stockwatch,dictionary,exchange)
##                Stockwatch.buttonclick(setposition)
##                Dictionary.buttonclick(setposition)
##                Exchange.buttonclick(setposition)
##                clickaccount = (Account.buttonclick(setposition))#Sets variables equal to their return value True or False
##                clickstockwatch = (Stockwatch.buttonclick(setposition))
##                clickdictionary = (Dictionary.buttonclick(setposition))
##                clickexchange = (Exchange.buttonclick(setposition))
##                if clickaccount == True:#If the account button was clicked access the account while loop only
##                    instockwatch = False
##                    inmenu = False
##                    indictionary = False
##                    inexchange = False
##                    inaccount = True
##                elif clickstockwatch == True:#If the stockwatch button was clicked access the stockwatch while loop only
##                    inmenu = False
##                    inaccount = False
##                    indictionary = False
##                    inexchange = False
##                    instockwatch = True
##                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
##                    inmenu = False
##                    inaccount = False
##                    inexchange = False
##                    instockwatch = False
##                    indictionary = True
##                elif clickexchange == True:#If the exchange button was clicked access the exchange while loop only
##                    inaccount = False
##                    inmenu = False
##                    instockwatch = False
##                    indictionary = False
##                    inexchange = True
##                
##        update()        
##        pygame.display.update()
        
##    while inaccount: #Main while loop for the account section of the game
##
##        
##        ##Fills the screen##
##        win.fill(GREY)
##        intermediate.fill(GREY) #Intermediate screen replaces the main window and is used for scrolling
##        ##--------------------##
##
##        #Creates the main buttons located on top of the screen#
##        Account =  stockclass.Button(win,(20,0,270,70),BLACK,"Account",WHITE)
##        Account.createbutton()
##        Stockwatch = stockclass.Button(win,(310,0,270,70),BLACK,"Stockwatch",WHITE)
##        Stockwatch.createbutton()
##        Dictionary = stockclass.Button(win,(600,0,270,70),BLACK,"Dictionary",WHITE)
##        Dictionary.createbutton()
##        Exchange = stockclass.Button(win,(890,0,270,70),BLACK,"Exchange",WHITE)
##        Exchange.createbutton()
##        ##-----------------------------------------------------##
##
##        
##        ##Manages the user bank information##
##        userbank =  stockclass.Bankaccount(win,1000,0,400,500)
##        userbank.initialfunds()
##        userbank.addfunds(2.30,200) #adds funds (Sharevalue, amount of shares)
##        userbank.displaycurrentfunds()
##        
##        userbank.addfunds(200,2)
##        userbank.changingfunds() #Prevents previous funds from being displayed (Blits a rectangle with same screen color over previous data at the same spot)
##        userbank.displaycurrentfunds()
##        
##        userbank.addfunds(10,5)
##        userbank.changingfunds()
##        userbank.displaycurrentfunds() #3 tested entries of adding stocks
##        
##        #pygame.display.update()
##        ##--------------------------------------------------------------------##
##
##        ##Manage events for the game##
##        for event in pygame.event.get():
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                setposition = pygame.mouse.get_pos()
##                Account.buttonclick(setposition) #Sets up buttonclick functionality for the 4 main buttons (account,stockwatch,dictionary,exchange)
##                Stockwatch.buttonclick(setposition)
##                Dictionary.buttonclick(setposition)
##                Exchange.buttonclick(setposition)
##                clickaccount = (Account.buttonclick(setposition)) #Sets variables equal to their return value True or False
##                clickstockwatch = (Stockwatch.buttonclick(setposition))
##                clickdictionary = (Dictionary.buttonclick(setposition))
##                clickexchange = (Exchange.buttonclick(setposition))
##                if clickaccount == True: #If the account button was clicked access the account while loop only
##                    instockwatch = False
##                    inmenu = False
##                    indictionary = False
##                    inexchange = False
##                    inaccount = True
##                elif clickstockwatch == True:#If the stockwatch button was clicked access the stockwatch while loop only
##                    inmenu = False
##                    inaccount = False
##                    indictionary = False
##                    inexchange = False
##                    instockwatch = True
##                elif clickdictionary == True: #If the dictionary button was clicked access the dictionary while loop only
##                    inmenu = False
##                    inaccount = False
##                    inexchange = False
##                    instockwatch = False
##                    indictionary = True
##                elif clickexchange == True:#If the exchange button was clicked access the exchange while loop only
##                    inaccount = False
##                    inmenu = False
##                    instockwatch = False
##                    indictionary = False
##                    inexchange = True
##
##        update()        
##        pygame.display.update()
##        ##---------------------------##


## Scrolling Mechanic##
##                    
##                if event.button == 4: #Events to scroll through the window
##                    scroll_y = min(scroll_y + 15,0)
##                if event.button == 5:
##                    scroll_y = max(scroll_y - 15, -500)
##        win.blit(intermediate,(0,scroll_y)) #Prevents the screen from flickering
##        pygame.display.flip()
##        clock.tick(60)
##--------------------##
