import pygame
pygame.init()

#game works 

#stock market class
#has the whole market
#method to generate a single stock, which then adds it to the whole stock market list that can be accessed
#

class stock_market(object):
    def __init__(self,data):
        self.data = data
        self.stocks = []
    #give this class ability to add a whole new stock, its properties and add values to that stock
    def add_stock(self,stock):
        self.stocks.append(stock)

    def display(self):
        for i in stocks:
            print("\nN:",i,"DB-C:",str(i.data.len()))
            for g in i.data: 
                print("\tDATE:",g.name,"OPEN:",g.val_open,"CLOSE:",g.val_close,"VOL",g.volume)

#individual stock generation class
#

class accum_stock(object):
    def __init__(self,ticker):
        self.ticker = ticker
        self.data = []
        
    def add_data(self,data):
        self.data.append(data)
    
    def fetch(self,date):
        for i in self.data:
            if i.name == date:
                return i

    def __str__(self):
        return self.ticker
    __repr__ = __str__
        
class stock_data(accum_stock):
    def __init__(self,date_time,val_open,val_close,volume):
        self.name = date_time
        self.val_open = val_open
        self.val_close = val_close
        self.volume = volume        
                      
    def __str__(self):
        return self.name
    __repr__ = __str__

        
#https://www.investopedia.com/university/stocks/stocks6.asp
#figure out live stock data
