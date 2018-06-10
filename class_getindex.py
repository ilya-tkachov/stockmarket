#http://pandas.pydata.org/pandas-docs/version/0.12/io.html
import pandas
import os
import random
import pandas_datareader
from class_stockdata import *
from datetime import datetime
from pathlib import Path

time = print() #realtime time
smbls = 8576
exclude = ["atest","ntest", "test", "z", "cbx",".","$","HJLI"]

market = None #north_america, asia, europe

north_america = {"DOWJONES":[],"S&P500":[],"NASDAQ_COMPOSITE":[],"NYSE":[]}
asia = {"NIKKEI":[],"TOPIX":[],"HANG_SENG":[],"CSI300":[]}
europe = {"S&P_EUROPE":[],"EURO_STOXX":[]}
#######Automatically retrieve indexes and the stocks inside them
#######CURRENCY CONVERTER


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

#quotes = {"S&P500":[],"FTSE100":[],"NASDAQ_RANDOM_500":generate_numbers(smbls),"NASDAQ_RANDOM_100":generate_numbers(smbls)}


def f_nasdaq():
    global nasdaq
    print("...Process Started...")
    print("...Checking NASDAQ File...")
    if Path(os.getcwd()+"\\_index\\north_america\\nasdaq\\symbols.txt").exists():
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
        rt_time = datetime.strptime(str(rx.values[13][0]), "%Y-%m-%dT%H:%M:%SZ")
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

def update_realtime_prices(m):#needs to account for US holidays
        cur_time = datetime.utcnow()
        if datetime.weekday(cur_time) < 5:
            if datetime.time(cur_time) > datetime.time(1,30,0,0) and datetime.time(cur_time) < datetime.time(20,0,0,0):
                print("\n...Updating Prices...")
                for i in m.data:
                    rx = pandas_datareader.robinhood.RobinhoodQuoteReader(i.ticker).read()
                    rt_price = rx.values[8][0]
                    rt_time = datetime.strptime(str(rx.values[13][0]), "%Y-%m-%dT%H:%M:%SZ")
                    #pandas_datareader.robinhood.RobinhoodQuoteReader(str(nasdaq.index[i.index_num])).read().to_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.index[i.index_num])+".csv"),header=False,index=False)
                    #sx = pandas.read_csv(str(os.getcwd()+"\\_index\\nasdaq\\_shares\\"+str(nasdaq.index[i.index_num])+".csv"),index_col=0)
                    i.update(rt_price,rt_time)
                print("...Updated Prices Successfully...")
                print("...Real Time:",m.data[0].time())
            else:
                print("...Market is closed; Please try between 9:30am EST and 4:00PM...")
        else:
            print("...Market is closed on the weekend...")
f_nasdaq()
shares = generate_numbers(smbls)
m = market()

#update_realtime_prices()

    

    
