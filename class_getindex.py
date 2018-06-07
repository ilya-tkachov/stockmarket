import pandas
import os
import pandas_datareader
from class_stockdata import *
#from pandas_datareader import data, wb
from datetime import datetime

nasdaqfile = pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"))
nasdaq = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"),usecols=["Symbol"])
#pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(path_or_buf="E:\Comp Sci\final project\_index\nasdaq\symbols.txt")
shr = "NVDA"
a = pandas_datareader.robinhood.RobinhoodQuoteReader({shr}).read().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),header=False,index=False)#str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),cols="last_trade_price")#header=False,index=False)
b = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),index_col=0) #usecols=['last_trade_price','updated_at']
#pandas.to_string -------<<<<<<<< USE INSTEAD AT http://pandas.pydata.org/pandas-docs/version/0.12/io.html

#print(b.index[7])
#print(b.index[12])
#print(nasdaq.Symbol[7])

time = print() #realtime time
smbls = 8576
#http://pandas.pydata.org/pandas-docs/version/0.12/io.html
def nasdaq():
    print("...Process Started...")
    print("...Getting NASDAQ File...")
    nasdaq_file = pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"))
    nasdaq = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\symbols.txt"),usecols=["Symbol"])
    print("...Got NASDAQ File...")

    print("...Getting",str(smbls),"Quotes...")
    for i in smbls:
        print()
    #market = stock_market
