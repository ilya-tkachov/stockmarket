import pygame
from datetime import datetime
#from datetime import datetime
pygame.init()

#game works 

#stock market class
#has the whole market
#method to generate a single stock, which then adds it to the whole stock market list that can be accessed
#

class stock_market(object):
    def __init__(self,data):
        self.data = data
    #give this class ability to add a whole new stock, its properties and add values to that stock
    def add_stock(self,stock):
        self.stocks.append(stock)

    def fetch(self,name):
        for i in self.data:
            if i.ticker == name:
                return i

#individual stock generation class
#

class accum_stock(object):
    def __init__(self,ticker,rt_price,rt_time):
        self.ticker = ticker
        self.info = [[rt_price,rt_time]]
        ##self.rt_price = rt_price
        ##self.rt_time = rt_time
        self.data = []
        
    def add_data(self,data):
        self.data.append(data)

    def price(self):
        return self.info[-1][0]

    def time(self):
        return self.info[-1][1].strftime("%r")
    
    def pull_history(self,d,m,y):
        for i in self.data:
            if i.date == datetime.date(datetime(y,m,d)):
                return i

    def chg(self,chg): #for statistical purposes
        if chg == "now":
            return price()/self.info[-2][0]
        elif chg == "1d":
            return price() - data[-1].close_price
        elif chg == "year":
            return price()/data[0].close_price
        
    def update(self,p,t):
        self.info.append([rt_price,rt_time])
    
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

        
#https://www.investopedia.com/university/stocks/stocks6.asp
#figure out live stock data
