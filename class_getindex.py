import pandas
import os
import pandas_datareader
from class_stockdata import *
#from pandas_datareader import data, wb
from datetime import datetime
#nasdaq = [["NVDA",[["2017-11-08",1,2,200],["2017-12-08",2,3,201],["2017-13-08",3,4,202]]],["TSLA",[["2017-11-08",1,2,200],["2017-12-08",2,3,201]]]
nasdaq = pandas_datareader.nasdaq_trader.get_nasdaq_symbols()
#pandas_datareader.nasdaq_trader.get_nasdaq_symbols().to_csv(path_or_buf="E:\Comp Sci\final project\_index\nasdaq\symbols.txt")
shr = "NVDA"
a = pandas_datareader.robinhood.RobinhoodQuoteReader({shr}).read().to_string()#str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),cols="last_trade_price")#header=False,index=False)
#b = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(shr)+".csv"),index_col=0)
#pandas.to_string -------<<<<<<<< USE INSTEAD AT http://pandas.pydata.org/pandas-docs/version/0.12/io.html



print(a)
#print(b.index[7])
#print(b.index[12])
#print(b.ix[7])
#b = pandas.read_csv(a.))
#test = pandas_datareader.robinhood.RobinhoodQuoteReader("NVDA")
#pandas.read_csv(pandas_datareader.robinhood.RobinhoodQuoteReader("NVDA").read().to_csv())
time = print() #realtime time

#http://pandas.pydata.org/pandas-docs/version/0.12/io.html
def nasdaq():
    print()
    #market = stock_market
