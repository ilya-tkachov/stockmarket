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
#print(nasdaq.index[7])

time = print() #realtime time
smbls = 8576
exclude = ["atest","ntest", "test", "z", "cbx",".","$","HJLI"]

north_america = []
asia = []
europe = []
quotes = {"S&P500":[],"FTSE100":[],"NASDAQ_RANDOM_500":generate_numbers(smbls),"NASDAQ_RANDOM_100":generate_numbers(smbls)}
#######CURRENCY CONVERTER

#http://pandas.pydata.org/pandas-docs/version/0.12/io.html
def generate_numbers(smbls):
    lst = []
    s = 10
    print("\n...Getting Quotes")
    for i in range(0,s):
        g = random.randrange(0,smbls)
        if str(nasdaq.index[g]).isalpha() == False:
            print("...Cannot get",str(nasdaq.index[g]))
            s+=1
        else:
            lst.append(str(nasdaq.index[g]))
    print("...Got Quotes:")
    for v in lst:
        print(str(v))
    return lst

def f_nasdaq():
    global nasdaq
    print("...Process Started...")
    print("...Checking NASDAQ File...")
    if Path(os.getcwd()+"\\_index\\nasdaq\\symbols.txt").exists():
        print("...Found NASDAQ File, Skipping...")
    else:
        print("...Cannot Find File, Getting NASDAQ...")
        nasdaq_file = pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"))
        print("...Got NASDAQ File...")
    #nasdaq = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"),usecols=["Symbol"],converters={"$":""})
    nasdaq = pandas_datareader.nasdaq_trader.get_nasdaq_symbols()
    #for i in shares:
        #pandas_datareader.robinhood.RobinhoodQuoteReader(str(nasdaq.index[i])).read().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.index[i])+".csv"),header=False,index=False)
        #print("...Retrieved",str(nasdaq.index[i]))
    
def market():
    data = []
    print("\n...Creating Stock Market...")
    for i in shares:
        print("\n...Adding",i,"To Stock Market")
        #sx = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.index[i])+".csv"),index_col=0)
        print("...Getting Quote from Robinhood...")
        rx = pandas_datareader.robinhood.RobinhoodQuoteReader(i).read()
        rt_price = rx.values[8][0]
        rt_time = rx.values[13][0]
        temp_stock = accum_stock(i,rt_price,rt_time)
        print("......Fetching Historical Data...")
        dx = pandas_datareader.DataReader(i, 'robinhood')
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
        print(".........Fetched",temp_stock.data[0],";",temp_stock.data[max_range-1])
        data.append(temp_stock)
        print("......Added Yearly Data Successfully...")
        #len(dx.head().index.levels[1]) --length
        #dx.head().index.levels[1][0].date() ---time
        #dx.head().get_value(dx.head().index[0],"open_price") ----close_price, open_price, volume
    m = stock_market(data)
    print("\n...Created Stock Market Successfully...")
    return m

def update_realtime_prices(m):
    print("\n...Updating Prices...")
    for i in m.data:
        rx = pandas_datareader.robinhood.RobinhoodQuoteReader(i.ticker).read()
        rt_price = rx.values[8][0]
        rt_time = rx.values[13][0]
        #pandas_datareader.robinhood.RobinhoodQuoteReader(str(nasdaq.index[i.index_num])).read().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.index[i.index_num])+".csv"),header=False,index=False)
        #sx = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.index[i.index_num])+".csv"),index_col=0)
        i.update(rt_price,rt_time)
    print("...Updated Prices Successfully...")
    print("...Real Time:",m.data[0].time())



f_nasdaq()
shares = generate_numbers(smbls)
m = market()

#update_realtime_prices()


    
