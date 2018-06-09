import pandas
import os
import random
import pandas_datareader
from class_stockdata import *
#from pandas_datareader import data, wb
from datetime import datetime
from pathlib import Path

#nasdaqfile = pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"))
#nasdaq = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"),usecols=["Symbol"])
#pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(path_or_buf="E:\Comp Sci\final project\_index\nasdaq\symbols.txt")
#a = pandas_datareader.robinhood.RobinhoodQuoteReader({shr}).read().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),header=False,index=False)#str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),cols="last_trade_price")#header=False,index=False)
#b = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),index_col=0) #usecols=['last_trade_price','updated_at']
#pandas.to_string -------<<<<<<<< USE INSTEAD AT http://pandas.pydata.org/pandas-docs/version/0.12/io.html

#print(b.index[7])
#print(b.index[12])
#print(nasdaq.Symbol[7])

time = print() #realtime time
smbls = 8576
exclude = ["atest","ntest", "test", "z", "cbx",".","$","HJLI"]

#http://pandas.pydata.org/pandas-docs/version/0.12/io.html
def generate_numbers(smbls):
    lst = []
    s = 10
    print("\n...Getting Quotes")
    for i in range(0,s):
        g = random.randrange(0,smbls)
        if str(nasdaq.Symbol[g]).isalpha() == False:
            print("...Cannot get",str(nasdaq.Symbol[g]))
            s+=1
        else:
            lst.append(g)
    print("...Got Quotes:")
    for v in lst:
        print(str(v),";",str(nasdaq.Symbol[v]))
    return lst

def f_nasdaq():
    global nasdaq
    global shares
    print("...Process Started...")
    print("...Checking NASDAQ File...")
    if Path(os.getcwd()+"\\_index\\nasdaq\\symbols.txt").exists():
        print("...Found NASDAQ File, Skipping...")
    else:
        print("...Cannot Find File, Getting NASDAQ...")
        nasdaq_file = pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"))
        print("...Got NASDAQ File...")
    nasdaq = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"),usecols=["Symbol"],converters={"$":""})
    shares = generate_numbers(smbls)
    for i in shares:
        pandas_datareader.robinhood.RobinhoodQuoteReader(str(nasdaq.Symbol[i])).read().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.Symbol[i])+".csv"),header=False,index=False)
        print("...Retrieved",str(nasdaq.Symbol[i]))
    
def market():
    data = []
    hist = []
    print("\n...Creating Stock Market...")
    for i in shares:
        print("\n...Adding",str(nasdaq.Symbol[i]),"To Stock Market")
        sx = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.Symbol[i])+".csv"),index_col=0)
        temp_stock = accum_stock(str(nasdaq.Symbol[i]),sx.index[7],sx.index[12])
        print("......Fetching Historical Data...")
        dx = pandas_datareader.DataReader(str(nasdaq.Symbol[i]), 'robinhood')
        print("......Fetched Historical Data...")
        print(".........Adding Yearly Data...")
        max_range = len(dx.head().index.levels[1])
        for indx in range(0,max_range):
            date = dx.head(max_range).index.levels[1][indx].date()
            open_price = dx.head(max_range).get_value(dx.head(max_range).index[indx],"open_price")
            close_price = dx.head(max_range).get_value(dx.head(max_range).index[indx],"close_price")
            volume = dx.head(max_range).get_value(dx.head(max_range).index[indx],"volume")
            temp_hist = stock_data(date,open_price,close_price,volume)
            temp_stock.add_data(temp_hist)
        print(".........Fet ched",temp_stock.data[0],";",temp_stock.data[max_range-1])
        data.append(temp_stock)
        print("......Added Yearly Data Successfully...")
        #len(dx.head().index.levels[1]) --length
        #dx.head().index.levels[1][0].date() ---time
        #dx.head().get_value(dx.head().index[0],"open_price") ----close_price, open_price, volume
    m = stock_market(data)
    print("\n...Created Stock Market Successfully...")
    return m
    
f_nasdaq()
m = market()

#m.fetch("NTEC").pull_history(18,7,2017)
    
