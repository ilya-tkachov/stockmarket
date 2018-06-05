import pygame
import math
import random
pygame.init()

class stock(object):
    def __init__(self,screen,rect,companyname,linecolour,xaxis,yaxis):
        self.screen = screen
        self.rectx = rect[0]
        self.recty = rect[1]
        self.rectwidth = rect[2]
        self.rectheight = rect[3]
        self.companyname = companyname
        self.linecolour = linecolour
        self.xaxis = xaxis
        self.yaxis = yaxis
        
    def createdatadisplay(self,rectcolour):
        pygame.draw.rect(self.screen,rectcolour,(self.rectx,self.recty,self.rectwidth,self.rectheight))
        companytext = pygame.font.SysFont("arial",self.rectwidth // 10)
        textsurface = companytext.render(self.companyname,True,(255,0,0))
        textsurface_rect = textsurface.get_rect(center = (self.rectx + self.rectwidth//2,self.recty + self.rectheight + self.rectheight//5))
        self.screen.blit(textsurface,textsurface_rect)
        

    def createvisualdata(self,width):
        n = 0
        x = self.rectx
        y = self.recty + (self.rectheight//2)
        #print(x,y)
        weeklyoutcome = []
        for i in range(80):
            i = random.randrange(-100,100)
            weeklyoutcome.append(i)
        d = (-math.pi/4)
        if n == 10:
            return False
        else:
            for i in weeklyoutcome:
                if i < 0 and d < 0:
                    d = -1 * d 
                elif d > 0 and i > 0:
                    d = -1 * d 
                length = self.rectwidth// 52
                x2 = int(x+length*math.cos(d))
                y2 = int(y+length*math.sin(d))
                n+= 1
                pygame.draw.line(self.screen,self.linecolour,(x,y),(x2,y2),width)
                #print(d)
                pygame.time.delay(0)
                x = x2
                y = y2
                if y2 >= self.recty:
                    i = 0
                pygame.display.update()

    def createaxis(self):
        spacer = self.rectx
        yspacer = self.rectx
        ylocation =  self.recty + self.rectheight
        newylocation = self.recty + self.rectheight
        xlist = []
        for i in range(0,53,4):
            xlist.append(i)
        for z in xlist:
            companyxaxis = pygame.font.SysFont("arial",self.rectwidth // 24)
            newtextsurface = companyxaxis.render(str(z),True,(255,0,0))
            if len(str(z)) > 1:
                spacer = spacer + self.rectwidth // 60
            self.screen.blit(newtextsurface,(spacer,ylocation))
            spacer += self.rectwidth // 17
        ylist = []
        for a in range(50,101,50):
            ylist.append(a)
        for q in ylist:
            companyyaxis = pygame.font.SysFont("arial",self.rectwidth//24)
            ytextsurface = companyyaxis.render(str(q),True,(255,0,0))
            newylocation -= self.rectheight //2 
            self.screen.blit(ytextsurface,(yspacer,newylocation))


            

