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

##    def display(self):
##        for i in self.data:
##            print("\nN:",i,"DB-C:",str(i.data.len()))
##            for g in i.data: 
##                print("\tDATE:",g.name,"OPEN:",g.val_open,"CLOSE:",g.val_close,"VOL",g.volume)

#individual stock generation class
#

class accum_stock(object):
    def __init__(self,ticker,rt_price,rt_time):
        self.ticker = ticker
        self.rt_price = rt_price
        self.rt_time = rt_time
        self.data = []
        
    def add_data(self,data):
        self.data.append(data)

    def price(self):
        return self.rt_price

    def time(self):
        return self.rt_time
    
    def pull_history(self,d,m,y):
        for i in self.data:
            if i.date == datetime.date(datetime(y,m,d)):
                return i

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
