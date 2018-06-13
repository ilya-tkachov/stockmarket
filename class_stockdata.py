import pygame
from datetime import datetime
pygame.init()

class stock_market(object):
    def __init__(self,data):
        self.data = data
    def add_stock(self,stock):
        self.stocks.append(stock)

    def fetch(self,name):
        for i in self.data:
            if i.ticker == name:
                return i

class accum_stock(object):
    def __init__(self,ticker,rt_price,rt_time,name=None):
        self.ticker = ticker
        self.info = [[rt_price,rt_time]]
        self.name = name
        self.data = []
        
    def add_data(self,data):
        self.data = data

    def price(self):
        return float(self.info[-1][0])

    def time(self):
        return self.info[-1][1].strftime("%I:%M %p")
    
    def pull_history(self,d,m,y):
        for i in self.data:
            if i.date == datetime.date(datetime(y,m,d)):
                return i

    def chg(self,chg): #for statistical purposes
        if chg == "now":
            return self.price()/float(self.info[-2][0])
        elif chg == "1d":
            return self.price()-self.data[-1].close_price
        elif chg == "year":
            if self.price() > self.data[0].close_price:
                return "+"+str(((self.price()-self.data[0].close_price)/self.data[0].close_price)*100)
            elif self.price() < self.data[0].close_price:
                return "-"+str(((self.data[0].close_price-self.price())/self.data[0].close_price)*100)
            
    def update(self,p,t):
        self.info.append([p,t])
    
    def __str__(self):
        return self.ticker
    __repr__ = __str__
        
class stock_data(accum_stock): #ability to retrieve database prices
    def __init__(self,date,open_price,close_price,volume): 
        self.date = date
        self.open_price = open_price
        self.close_price = close_price
        self.volume = volume
        
    def __str__(self):
        return self.date.strftime("%B %d, %Y")
    __repr__ = __str__
