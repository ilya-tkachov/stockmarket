import pygame
import math
import random
pygame.init()

class stock(object): #Initial stock class that will create the visual display of live stock data
    def __init__(self,screen,rect,companyname,linecolour,xaxis,yaxis): #Initializes all assets needed to create the componenets of the class
        self.screen = screen #Initializes all parameters
        self.rectx = rect[0]
        self.recty = rect[1]
        self.rectwidth = rect[2]
        self.rectheight = rect[3]
        self.companyname = companyname
        self.linecolour = linecolour
        self.xaxis = xaxis
        self.yaxis = yaxis
        
    def createdatadisplay(self,rectcolour): #Creates and displays the rectangle and company name with a rectcolour parameter
        pygame.draw.rect(self.screen,rectcolour,(self.rectx,self.recty,self.rectwidth,self.rectheight)) #Draws the rectangle with the rect properties first initialized
        companytext = pygame.font.SysFont("arial",self.rectwidth // 10) #Creates the company text attributes (font and size)
        textsurface = companytext.render(self.companyname,True,(255,0,0)) #Creates the text surface and renders the company text
        textsurface_rect = textsurface.get_rect(center = (self.rectx + self.rectwidth//2,self.recty + self.rectheight + self.rectheight//5)) #Creates the x and y properties for the center of the rectangle
        self.screen.blit(textsurface,textsurface_rect) #Blits the text onto the screen (textsurface, (x,y))
        

    def createvisualdata(self,width): #Creates the line that represents the fluctuation of stock data over time
        n = 0 #Parameter that will be used to stop the line from drawing at a certain point
        x = self.rectx #initial x value of the line
        y = self.recty + (self.rectheight//2) #Initial y value of the line (starts at the left most center of the rectangle
        weeklyoutcome = [] #empty list that will be used for the stock data
        for i in range(80): #Creates a list of 80 integers with values that range from -100 to 100
            i = random.randrange(-100,100)
            weeklyoutcome.append(i) #appends each i character to the list
        d = (-math.pi/4) #Initial angle of the stock 
        if n == 10: #When the n parameter reaches the value of 10, it will return false to stop drawing the line
            return False
        else:
            for i in weeklyoutcome: #For loop to iterate through the list containing stock info for that given company
                if i < 0 and d < 0: #Ensures that the line will go up and down depending on the stock data
                    d = -1 * d 
                elif d > 0 and i > 0:
                    d = -1 * d 
                length = self.rectwidth// 52 #Length of each drawn line
                x2 = int(x+length*math.cos(d)) #Determines the end points of the line being drawn
                y2 = int(y+length*math.sin(d))
                n+= 1 #Increments the paramater by a value of 1 through each line drawn
                pygame.draw.line(self.screen,self.linecolour,(x,y),(x2,y2),width) #Code that draws the line onto the screen
                pygame.time.delay(0) #Delays events in ms everytime the line is drawn
                x = x2 #Starts the next line on the endpoints of the previous line
                y = y2
                if y2 >= self.recty: #Ensures the line never crosses above the rectangle
                    i = 0
                pygame.display.update() #Updates display

    def createaxis(self): #Creates the x and y axis for the rectangle
        spacer = self.rectx #The x location for the values in the x axis
        yspacer = self.rectx #The x location for the values in the y axis
        ylocation =  self.recty + self.rectheight #The y location for the values in the x axis
        newylocation = self.recty + self.rectheight #The y locationn for the values in the y axis
        xlist = [] #Empty list that represents the weeks in the year
        for i in range(0,53,4):
            xlist.append(i) #Creates the list of weeks in the year from 0-52
        for z in xlist: #Iterates through the numbers in the list for the x axis
            companyxaxis = pygame.font.SysFont("arial",self.rectwidth // 24) #Initializes the font and size for the x axis components
            newtextsurface = companyxaxis.render(str(z),True,(255,0,0)) #Renders the text surface the x axis componenets
            if len(str(z)) > 1: #For numbers that are double digit or more
                spacer = spacer + self.rectwidth // 60 #Renders the space between each double digit number
            self.screen.blit(newtextsurface,(spacer,ylocation)) #Blits the x axis onto the screen
            spacer += self.rectwidth // 17 #Spaces each x component that are single digit 
        ylist = [] #The list of values for the y axis
        for a in range(50,101,50):
            ylist.append(a) #Creates the list of values in which range from 0-100 and increment by 50
        for q in ylist: #For loop that iterates through the ylist
            companyyaxis = pygame.font.SysFont("arial",self.rectwidth//24) #Renders the font for the y axis components
            ytextsurface = companyyaxis.render(str(q),True,(255,0,0)) #Renders the text surface for the y axis components
            newylocation -= self.rectheight //2 #spaces out each y component of the axis
            self.screen.blit(ytextsurface,(yspacer,newylocation)) #Blits the y values onto the screen


            
class Button(object): #Button class that will be used to create a button that can be displayed anywhere and used

    def __init__(self,screen,buttonrect,fillcolor = (69,139,0), bordercolor = (0,0,0),textsize =24): #Initializes the key parameters of the button class
        self.screen = screen
        self.buttonrectx = buttonrect[0]
        self.buttonrecty = buttonrect[1]
        self.buttonrectwidth = buttonrect[2]
        self.buttonrectheight = buttonrect[3]
        self.fillcolor = fillcolor
        self.bordercolor = bordercolor
        self.textsize = textsize
