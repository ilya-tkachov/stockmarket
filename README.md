# 
This is a stock market game.
To use class_stockdata.py:

class stock_market():
Available functions:

fetch():
Takes the name of the ticker, fetches it from its stock_market().data and outputs as a class that can be accessed. (Output all tickers inside the market by calling stock_market().data)

----------------------------------------------------------------------------------------------------------

class accum_stock():
Available functions:

add_data():
Add historical data. Must use stock_data class.

price():
Return the realtime price. Takes the [:-1] indice of self.info.

time():
Return the time of the price change in STRING format.

pull_history(d,m,y):
enter a day, month and year to retrieve stock prices of that current date, accessible through stock_data class variables.

chg():
--to be completed

----------------------------------------------------------------------------------------------------------

class stock_data(accum_stock):
A data structure for historical data. Once accessed through pull history, variable [date,open_price,close_price,volume] can be called for that time period.
Available functions: none

----------------------------------------------------------------------------------------------------------

To use class_getindex.py:

trade_currency(value,symbol_from,symbol_to):
value: take your current balance
symbol_from: take the symbol that the currency is at (ex. US - US Dollar)
symbol_to: take the symbol that you would like to convert to (ex. CH - Chinese Yuan)
Will output the conversion in CHINESE YUAN.

f_nasdaq():
Checks if the NASDAQ file exists on the computer. Crucial for retrieving symbols. Will create if absent.

market(shares):
Takes the list of shares and creates a stock market using predefined classes. 

fetch_history(temp_stock):
Take the name of the stock using fetch() function of class.stock_market and directly insert the historcal data ranging one year from TODAY

check_market_time():
Check if the market is open at this time.
9:30AM EST - 4:00PM EST
Program checks for 1:30PM UST - 8:00PM UST

update_realtime_prices()
Takes the name of the variable that the market class is assigned to and fetches online prices to add to the list.
