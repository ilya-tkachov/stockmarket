import pygame
import os
from class_stockdata import *
from class_getindex import *
import time
import os  

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init

#remove window border
#pygame crashing when looping the update?

maps = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\map.png")),(800,400))
asia = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\asia_isolate.png")),(800,400))
north_america = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\north_america_isolate.png")),(800,400))
europe = pygame.transform.scale(pygame.image.load(str(os.getcwd()+"\\_assets\\europe_isolate.png")),(800,400))

map_img = [maps,asia,europe,north_america]
ver = "v1-ri-ini"

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

win = pygame.display.set_mode((1200,800), pygame.NOFRAME)
win.fill((35,35,35))

pygame.draw.rect(win,(22,22,22),(200,200,800,400))
for i in map_img:
    win.blit(i,(200,200))
menu_bar = top_bar(win,[0,0,1200,15],(186,186,186),ver,"HH:MM:APM")

temp_time = time.time()
print("Select Continent")
print(continets)
c = input(":")
print("Select Market")
print(select_market(c))
smbls = select_index(select_market(c),input(":"))

f_nasdaq()
#shares = generate_numbers(smbls)
m = market(smbls)

while True:
    event = pygame.event.get()
    for x in event:
        if event is pygame.QUIT:
            pygame.quit()
            raise SystemExit
        else:
            if float(time.time()) >= float(temp_time)+62:
                update_realtime_prices(m)
                print("...Updated Prices...")
                temp_time = time.time()
            menu_bar.update(str(time.strftime("%I:%M%p [%S]")),check_market_time())
            pygame.display.update()
    
raise SystemExit

