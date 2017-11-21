# path = "/home/mar/Python/socratica/googlestockdata.csv"
# with open(path) as fileobject:
# 	contents = fileobject.read()
# 	print(contents) #prints without \n separating each line
# with open(path) as fileobject:
# 	for eachline in fileobject:
# 		print(eachline) #prints with \n separating each line
# lines = [line for line in open(path)]
# print(lines[0]) #print Date,Open,High,Low,Close,Volume,Adj Close
# print(lines[1]) #print 8/19/2014,585.002622,587.342658,584.002627,586.862643,978600,586.862643
# print(lines[0].strip()) #print Date,Open,High,Low,Close,Volume,Adj Close
# print(lines[0].strip().split(",")) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# print(lines[1].strip().split(",")) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']
# dataset = [line.strip().split(",") for line in open(path)]
# print(dataset[0]) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# print(dataset[1]) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']

import csv
from datetime import datetime
#print(dir(csv)) #print ['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']
path = "/home/mar/Python/socratica/googlestockdata.csv"
file = open(path, newline="")
reader = csv.reader(file)
header = next(reader) #the first line is the header
# data = [row for row in reader]
# print(header) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# print(data[0]) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']
data = []
for row in reader:
	#row = [Date, Open, High, Low, Close, Volume, Adj Close]
	date = datetime.strptime(row[0],"%m/%d/%Y")
	open_price = float(row[1]) #"open" is a built-in function
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = int(row[5])
	adj_close = float(row[6])
	data.append([date, open_price, high, low, close, volume, adj_close])
print(data[0]) #[datetime.datetime(2014, 8, 19, 0, 0), 585.002622, 587.342658, 584.002627, 586.862643, 978600, 586.862643]
returnspath = "/home/mar/Python/socratica/googlestockdata2.csv"
file = open(returnspath,"w")
writer = csv.writer(file)
writer.writerow(["Date","Return"])
for i in range(len(data)-1):
	todaysrow = data[i]	
	todaysdate = todaysrow[0]	
	todaysprice = todaysrow[-1]
	yesterdayrow = data[i+1]
	yesterdayprice = yesterdayrow[-1]
	dailyreturn = (todaysprice - yesterdayprice) / yesterdayprice
	formatteddate = todaysdate.strftime("%m/%d/%Y")
	writer.writerow([formatteddate, dailyreturn])
