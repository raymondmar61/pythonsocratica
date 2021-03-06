#Socratica 002 Hello world, 003 Introduction to Strings, 004 Numbers in Version 2, 005 Numbers in Version 3, 006 Arithmetic in Python V2, 007 Arithmetic in Python V3, 009 Booleans, 010 If then else, 011 Python Functions, 012 Sets in Python, 013 Python Lists, 014 Python Dictionaries, 015 Python Tuples, 

#Socratica New 027 Map, Filter, and Reduce Functions, New 010 Datetime Module (Dates and Times),  New 017 Logging in Python, New 019 Python Random Number Generator the Random Module, New 020 CSV Files in Python, New 021 A Random Walk & Monte Carlo Simulation, New 022 List Comprehension, New 024 Prime Numbers, New 023 Python Classes and Objects, New 026 Lambda Expressions & Anonymous Functions, New 025 JSON, New 028 Sorting

print("Hello world") #print Hello world
message = "Meet me tonight."
print(message) #print Meet me tonight.
message3 = 'I\'m looking for someone to share in an adventure.'
print(message3)
movie_quote_triplequotes = """One of my favorite lines from The Godfather is:  "I'm going to make him an offer he can't refuse.  Do you know who said this?"""
print(movie_quote_triplequotes) #print I'm looking for someone to share in an adventeure.  One of my favorite lines from The Godfather is:  "I'm going to make him an offer he can't refuse.  Do you know who said this?
print("\n")

print("Python version 2 types of numbers: int, long, float, complex")
a = 28
print(type(a)) #print <class 'int'>
e = 2.718281828
print(type(e)) #print <class 'float'>
z = 3 + 5.7j #j is used for i = square root of negative 1
print(type(z)) #print <class 'complex'>
print(z.real) #print 3.0
print(z.imag) #print 5.7
print("Python version 3 types of numbers: int, float, complex")
z = 2 - 6.1j
print(type(z)) #print <class 'complex'>
print(z.real) #print 2.0
print(z.imag) #print -6.1
x = 28
y = 39.0
print(x) #print 28
print(float(x)) #print 28.0
print(y) #print 39.0
print(int(y)) #print 39
a = 2
b = 6.0
c = 12 + 0j
#Combining two numbers of different types Python3.0 converts the narrower type to the wider type
print(a + b) #print 8.0
print(b - a) #print 4.0
print(a * 7) #print 14
print(c / b) #print (2+0j)
#However, division Python3.0 returns a float.  Use // to return an int.
print(16/4) #print 4.0
print(16/5) #print 3.2
print(16//4) #print 4
print(16//5) #print 3
print(16%5) #print 1
print("\n")

a = 3
b = 5
print(a == b) #print False
print(a != b) #print True
print(type(True)) #print <class 'bool'>
print(type(False)) #print <class 'bool'>
print(bool("")) #print False
print(bool(0)) #print False
print(5 + True) #print 6
print("\n")

input = "strin"
if len(input) < 6:
	print("Your string is too short.")
	print("Please enter a string with at least 6 characters.")
inputnumber = 50.7 #50.7 returns Your number is even
number = int(inputnumber)
if number % 2 == 0:
	print("Your number is even.")
else:
	print("Your number is odd.")
#Scalene all triangle sides are different. Isosceles two sides are same.  Equilateral all triangle sides are same.
aside = 3
bside = 4
cside = 5
if (a != b) and (b != c) and (a != c):
	print("This is a scalene triangle.")
elif (a==b) and (b==c):
	print("This is an equilateral triangle.")
else:
	print("This is an isosceles triangle.")
#BTW, how do we know the three sides are a triangle?  a^2 + b^2 = c^2?
print("\n")

def f():
	pass
print(f()) #print None
def ping():
	return "Ping!"
print(ping()) #print Ping!
#Volume of a sphere is V=4/3(pi)r^3
import math
print(math.pi) #print 3.141592653589793
def volume(r):
	"""doc string for a function-->Returns the volume of a sphere with radius r."""
	v = (4.0/3.0) * math.pi * r**3
	return v
print(volume(2)) #print 33.510321638291124
#print(help(volume)) #print Help on function volume in module __main__:
#volume(r)
#    doc string for a function-->Returns the volume of a sphere with radius r.
print(volume(15)) #print 14137.166941154068
#Area of a triangle is A = (1/2)(b)(h)
def trianglearea(b, h):
	"""doc string for a function-->Returns the area of a triangle with base b and height h."""
	return 0.5 * b * h
print(trianglearea(3,6)) #print 9.0
#keyword arguments or kwargs or default arguments
#1 inch = 2.54 cm.  1 foot = 12 inches
def cm(feet = 0, inches = 0):
	"""Converts a length from feet and inches to centimeters."""
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm
print(cm(feet = 5)) #print 152.4
print(cm(inches = 70)) #print 177.8
print(cm(feet = 5, inches = 8)) #print 172.72
print(cm(inches = 8, feet = 5)) #print 172.72
#keyword arguments must be last when using keyward arguments and required arguments
def g(y, x = 0):
	return (x + y)
print(g(17)) #print 17
print(g(17, 60)) #print 77
print(g(x=60,y=17)) #print 77
print("\n")

example = set()
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
print(example) #print {False, 42, 3.14159, 'Thorium'} in any order
print(len(example)) #print 4
example.remove(42)
print(example) #print {False, 3.14159, 'Thorium'} in any order
example.add(42)
print(example) #print {False, 42, 3.14159, 'Thorium'} in any order
example.discard(42)
print(example) #print {False, 3.14159, 'Thorium'} in any order
example2prepopulated = set([28, True, 2.71828, "Helium"])
print(len(example2prepopulated)) #print 4
example2prepopulated.clear()
print(len(example2prepopulated)) #print 0
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])
print(odds.union(evens)) #print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(evens.union(odds)) #print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(odds.intersection(primes)) #print {3, 5, 7}
print(evens.intersection(primes)) #print {2}
print(2 in primes) #print True
print(6 in odds) #print False
print("\n")

primeslist = [2, 3, 5, 7, 11, 13]
primeslist.append(17)
primeslist.append(19)
print(primeslist) #print [2, 3, 5, 7, 11, 13, 17, 19]
print(primeslist[0]) #print 2
print(primeslist[3]) #print 7
print(primeslist[-1]) #print 19
print(primeslist[-2]) #print 17
print(primeslist[2:5]) #print [5, 7, 11]
examplelist = [123, True, "Alpha", 1.732, [64, False]]
numberslist = [1, 2, 3]
letterslist = ["a","b","C"]
print(numberslist + letterslist) #print [1, 2, 3, 'a', 'b', 'c']
print(letterslist + numberslist) #print ['a', 'b', 'c', 1, 3, 4
print("\n")

#dictionary inputs are keys, outputs are values
post = {"user_id": 209, "message": "D5 E5 C4 C4 G4", "language": "English", "datetime": "20230215T124231Z", "location": (44.590533, -104.715556)}
print(type(post)) #print <class 'dict'>
print(post["message"]) #print D5 E5 C4 C4 G4
post2 = dict(message="SS Cotopaxi", language="English") #notice no quotes for the keys and notice dict()
print(post2) #print {'language': 'English', 'message': 'SS Cotopaxi'}
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2) #print {'datetime': '19771116T093001Z', 'language': 'English', 'message': 'SS Cotopaxi', 'user_id': 209}
try:
	print(post2["location"])
except KeyError:
	print("The post does not have a location") #print The post does not have a location
for eachkey in post.keys():
	print(eachkey)
	print(eachkey, "=", post[eachkey])
for key, value in post.items():
	print(key, "=", value)
print("\n")

prime_numbers = [2, 3, 5, 7, 11, 13, 17]
perfect_squares = (1, 4, 9, 16, 25, 36)
print("# Primes =",len(prime_numbers)) # Primes = 7
print("# Squares =",len(perfect_squares)) # Squares = 6
for p in prime_numbers:
	print("Prime:",p)
for n in perfect_squares:
	print("Square:",n)
print("Lists can add data, remove data, and change data.  Tuples can't be changed.  Tuples are immutable.")
empty_tuple = ()
test1a = ("a")
test1 = ("a",)
test2 = ("a","b")
test3 = ("a","b","c")
print(empty_tuple) #print ()
print(test1a) #print a
print(test1) #print ("a",)
print(test2) #print ("a","b")
print(test3) #print ("a","b","c")
survey = (27, "Vietnam", True)
age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age =", age) #print Age = 27
print("Country =", country) #print Country = Vietnam
print("knows python?", knows_python) #print knows python? True
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age =", age) #print Age = 21
print("Country =", country) #print Country = Switzerland
print("knows python?", knows_python) #print knows python? False
print("\n")

from math import pi
def area(r):
	return math.pi*(r**2)
radii = [2,5,7.1,0.3,10]
areas = []
for eachradii in radii:
	areas.append(area(eachradii))
print(areas) #print [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793]
print(map(area,radii)) #print <map object at 0x7faf69af76d8>
print(list(map(area,radii))) #print [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793]
temps = [("Berlin",29),("Cairo",36),("Buenos Aires",19),("Los Angeles",26), ("Tokyo",27), ("New York",28),("London",22),("Beijin", 32)]
ctof = lambda data: (data[0], (9/5)*data[1] + 32)
print(list(map(ctof, temps))) #print [('Berlin', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokyo', 80.6), ('New York', 82.4), ('London', 71.6), ('Beijin', 89.6)]
# RM:  Added two for loops experiment.  eachtemps2 for loop works.
# for eachtemps in temps:
# 	print(eachtemps)
# updatetemps = []
# for eachtemps2 in temps:
# 	print(eachtemps2[0], (9/5)*eachtemps2[1] + 32)
# 	tuplelove = (eachtemps2[0], (9/5)*eachtemps2[1] + 32)
# 	print(tuple(tuplelove))
# 	updatetemps.append(tuplelove)
# print(updatetemps)
from statistics import mean
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
theaverage = mean(data)
print(theaverage) #print 2.183333333333333
print(filter(lambda x: x > theaverage, data)) #print <filter object at 0x7f83c03019e8>
print(list(filter(lambda x: x > theaverage, data))) #print [2.7, 4.1, 4.3]
print(list(filter(lambda x: x < theaverage, data))) #print [1.3, 0.8, -0.1]
countries = ["","Argentina","","Brazil","","Chile","","Colombia","","Ecuador","","","Venezuela"]
print(list(filter(None,countries))) #print ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Venezuela']
#reduce() function Python creator Guido van Rossum says for loop is more readable than functools.reduce()
from functools import reduce
data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x, y: x*y
print(reduce(multiplier,data)) #print 6469693230
product = 1
for x in data:
	product = product * x
print(product) #print 6469693230

import datetime
#print(dir(datetime)) #print ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_divide_and_round', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
#print(help(datetime.date))
guidovanrossum = datetime.date(1956, 1, 31)
print(guidovanrossum)
print(guidovanrossum.year) #print 1956
print(guidovanrossum.month) #print 1
print(guidovanrossum.day) # print 31
millinium = datetime.date(2000,1,1)
delta = datetime.timedelta(100)
print(millinium + delta) #print 2000-04-10
print(guidovanrossum.strftime("%A %B %d, %Y")) #print Tuesday January 31, 1956
message = "Guido van Rossum was born on {:%A %B %d, %Y}."
print(message.format(guidovanrossum)) #print Guido van Rossum was born on Tuesday January 31, 1956.
launchdate = datetime.date(2017, 3, 30)
launchtime = datetime.time(22, 27, 0)
launchdatetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launchdate) #print 2017-03-30
print(launchtime) #print 22:27:00
print(launchdatetime) #print 2017-03-30 22:27:00
print(launchtime.hour) #print 22
print(launchtime.minute) #print 27
print(launchtime.second) #print 0
print(launchdatetime.year) #print 2017
print(launchdatetime.month) #print 3
print(launchdatetime.day) #print 30
print(launchdatetime.hour) #print 22
print(launchdatetime.minute) #print 27
print(launchdatetime.second) #print 0
now = datetime.datetime.today()
print(now) #print 2017-11-16 19:06:49.767610
print(now.year) #print 2017
print("microseconds",now.microsecond) #print 767610
moonlanding = "7/20/1969"
#strptime is string parse time
moonlandingdatetime = datetime.datetime.strptime(moonlanding, "%m/%d/%Y") #I believe %m/%d/%Y refers to moonlanding = "7/20/1969" %m/%d/%Y 
print(moonlandingdatetime) #print 1969-07-20 00:00:00
print(type(moonlandingdatetime)) #print <class 'datetime.datetime'>
print(moonlandingdatetime.year) #print 1969
print("\n")

import logging
#print(dir(logging)) #print ['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', 'PlaceHolder', 'RootLogger', 'StrFormatStyle', 'StreamHandler', 'StringTemplateStyle', 'Template', 'WARN', 'WARNING', '_STYLES', '_StderrHandler', '__all__', '__author__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__status__', '__version__', '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter', '_defaultLastResort', '_handlerList', '_handlers', '_levelToName', '_lock', '_logRecordFactory', '_loggerClass', '_nameToLevel', '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConfig', 'captureWarnings', 'collections', 'critical', 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogRecordFactory', 'getLogger', 'getLoggerClass', 'info', 'io', 'lastResort', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 'root', 'setLogRecordFactory', 'setLoggerClass', 'shutdown', 'sys', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "/home/mar/Python/socratica/test.log", level=logging.DEBUG, format=log_format, filemode="w")
logger = logging.getLogger() #create log file test.log
logger.info("Out first message")
print(logger.level) #print 30 #notset 0 debut 10 info 20 warning 30 error 40 critical 50
logger.debug("This is a harmless debug message.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")
print("\n")

import random
#print(dir(random)) #print ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
#print(help(random.randint)) #print Help on method randint in module random:\n randint(a, b) method of random.Random instance\n Return random integer in range [a, b], including both end points.
for i in range(10):
	print(random.random())
def myrandom():
	#generate random numbers >=3 and <7.  multiply by 4 which is 3,4,5,6.  Add+3 for starting range
	return (4*random.random())+3
for i in range(0,10):
	print(myrandom())
for i in range(0,10):
	print(random.uniform(3,7)) #print random numbers >=3 and <7
#normal distribution bell curve mean and standard deviation normalvariate(mean,standard deviation)
for i in range(0,20):
	print(random.normalvariate(5,0.5))
for i in range(0,20):
	print(random.randint(1,6))
outcomes = ["rock","paper","scissors"]
for i in range(0,20):
	print(random.choice(outcomes))
print("\n")

# path = "/home/mar/Python/socratica/googlestockdata.csv"
# file = open(path)
# # for line in file:
# # 	print(line) #print each lin in googlestockdata.csv
# lines = [line for line in open(path)] #list comprehension.  #A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. Chapter 4 Python Crash Course ch4workingwithliststaketwo.py.
# print(lines[0]) #print Date,Open,High,Low,Close,Volume,Adj Close
# print(lines[1]) #print 8/19/2014,585.002622,587.342658,584.002627,586.862643,978600,586.862643
# print(lines[0].strip()) #print Date,Open,High,Low,Close,Volume,Adj Close
# print(lines[0].strip().split(",")) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# dataset = [line.strip().split(",") for line in open(path)]
# print(dataset[0]) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# print(dataset[1]) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']
# import csv
# from datetime import datetime
# #print(dir(csv)) #print ['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']
# path = "/home/mar/Python/socratica/googlestockdata.csv"
# file = open(path, newline="")
# reader = csv.reader(file)
# header = next(reader) #The first line is the header.  Assign the header row equal to header from next(reader)
# # data = [row for row in reader]
# # print(header) #print ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# # print(data[0]) #print ['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643']
# data = []
# for row in reader:
# 	date = datetime.strptime(row[0], "%m/%d/%Y")
# 	open_price = float(row[1])
# 	high = float(row[2])
# 	low = float(row[3])
# 	close = float(row[4])
# 	volume = int(row[5])
# 	adjclose = float(row[6])
# data.append([date, open_price, high, low, close, volume, adjclose])
# print(data[0]) #print [datetime.datetime(2004, 8, 19, 0, 0), 100.000168, 104.060182, 95.960165, 100.340176, 44871300, 50.119968]
# returnspath = "/home/mar/Python/socratica/googlestockdatareturns.csv"
# file = open(returnspath, "w")
# writer = csv.writer(file)
# writer.writerow(["Date","Return"])
# for i in range(len(data)-1):
# 	todaysrow = data[i]
# 	todaysdate = todaysrow[0]
# 	todaysprice = todaysrow[-1]
# 	yesterdaysrow = data[i+1]
# 	yesterdaysprice = yesterdaysrow[-1]	
# 	dailyreturn = (todaysprice - yesterdaysprice) / yesterdaysprice
# 	formatteddate = todaysdate.strftime("%m/%d/%Y")
# 	writer.writerow([formatteddate, dailyreturn])
# #RM: code not working

import random
def randomwalk(n):
	"""return coordinates after "n" block random walk."""
	x = 0
	y = 0
	for i in range(0,n):
		step = random.choice(["N","S","E","W"])
		if step == "N":
			y = y + 1
		elif step == "S":
			y = y - 1
		elif step == "E":
			x = x + 1
		else:
			x = x - 1
	return (x,y)
print(randomwalk(10))
for i in range(0,5):
	walk = randomwalk(5)
	#print(walk,"Distance from home = ",abs(walk[0]) + abs(walk[1]))
def randomwalk2(n):
	"""return coordinates after "n" block random walk."""
	x,y = 0,0	
	for i in range(0,n):
		(dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)]) #it seems dx is the left of the (,) and dy is the right of the (,). N is (0,1), S (0,-1), E (1,0), W (-1,0)
		#print("dx",dx,"dy",dy)
		x += dx
		y += dy
	return (x,y)
for i in range(0,5):
	walk = randomwalk2(10)
	print(walk,"Distance from home = ",abs(walk[0]) + abs(walk[1]))
#monte carlo simulation which is thousands of random trials
numberofwalks = 10000
for walklength in range(1,5):
	notransport = 0 #number of walks four or few blocks from home
	for i in range(0,numberofwalks):
		(x,y) = randomwalk2(walklength)
		#print("x",x,"y",y)
		distance = abs(x) + abs(y)
		if distance <= 4:
			notransport += 1
	notransportpercentage = float(notransport) / numberofwalks
	print("Walk size =",walklength, "/ % of no transport =",100*notransportpercentage)

#list comprehension [expression for variable in collection if test1 and test2]  
#list comprehension [expression for variable1 in collection1 and variable2 in collection2]
squares = []
for i in range(1, 11):
	squares.append(i**2)
print(squares) #print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares2 = [i**2 for i in range(1,11)]
print(squares2) #print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5) #print [1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0, 1, 4, 4, 1, 0]
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story" "Gone With The Wind", "Citizen Kane", "It's A Wonderful Life", "The Wizard Of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders Of The Lost Ark", 
"Groundhog Day", "Close Encounters Of The Third Kind"]
gmovies = []
for title in movies:
	if title.startswith("G"):
		gmovies.append(title)
print(gmovies) #print ['Gandhi', 'Gattaca', 'Ghostbusters', 'Good Will Hunting', 'Groundhog Day']
gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2) #print ['Gandhi', 'Gattaca', 'Ghostbusters', 'Good Will Hunting', 'Groundhog Day']
movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's A Wonderful Life", 1946), ("Gattaca", 1997), ("No Country For Old Men", 2007), ("Rear Window", 1954), ("The Lord Of The Rings:  The Fellowship Of The Ring", 2001), ("Groundhog Day", 1993), ("Close Encounters Of The Third Kind", 1977), 
("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders Of The Lost Ark", 1981)]
movies2001 = []
for key, value in movies2:
	if value > 2000:
		movies2001.append(key)
print(movies2001) #print ['Spirited Away', 'No Country For Old Men', 'The Lord Of The Rings:  The Fellowship Of The Ring', 'The Royal Tenenbaums', 'The Aviator']
movies20012 = [title for (title, year) in movies2 if year < 2000]
print(movies20012) #print ['Citizen Kane', "It's A Wonderful Life", 'Gattaca', 'Rear Window', 'Groundhog Day', 'Close Encounters Of The Third Kind', 'Raiders Of The Lost Ark']
vectorlist = [2, -3, 1]
print(4*vectorlist) #print [2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3, 1] or vectorlist+vectorlist+vectorlist+vectorlist.  Adding lists concatenates them.
wvectorlist = [4*x for x in vectorlist]
print(wvectorlist) #print [8, -12, 4]
#Cartesian product a={1,3} b={x,y} a*b={(1,x), (1,y), (3,x), (3,y)}
oddlist = [1, 3, 5, 7]
evenlist = [2, 4, 6, 8]
cartesianproduct = [(a,b) for a in oddlist for b in evenlist]
cartesianproductproduct = [a*b for a in oddlist for b in evenlist]
print(cartesianproduct) #print [(1, 2), (1, 4), (1, 6), (1, 8), (3, 2), (3, 4), (3, 6), (3, 8), (5, 2), (5, 4), (5, 6), (5, 8), (7, 2), (7, 4), (7, 6), (7, 8)]
print(cartesianproductproduct) #print [2, 4, 6, 8, 6, 12, 18, 24, 10, 20, 30, 40, 14, 28, 42, 56]
print(max(cartesianproductproduct)) #print 56
list1 = [1]
list2 = [2, 3]
list3 = [4, 5, 6]
list123 = [a*b*c for a in list1 for b in list2 for c in list3]
print(list123) #print [8, 10, 12, 12, 15, 18]
listall = [[1], [2, 3], [4, 5, 6]]
listallproduct = [a for a in listall]
print(listallproduct) #print [[1], [2, 3], [4, 5, 6]]

import math
import time
def isprimev1(n):
	if n == 1:
		return False #1 is not a prime number
	for d in range(2, n):
		if n % d == 0:
			return False
	return True
t0 = time.time()
for n in range(1, 11):
	print(n, isprimev1(n))
t1 = time.time()
print("Time required: ",t1-t0)
def isprimev2(n):
	if n == 1:
		return False #1 is not a prime number
	maxdivisor = math.floor(math.sqrt(n))
	for d in range(2, 1+maxdivisor):
		if n % d == 0:
			return False
	return True
t2 = time.time()
for n in range(1, 11):
	print(n, isprimev2(n))
t3 = time.time()
print("Time required v2: ",t3-t2)
t4 = time.time()
for n in range(1, 100001):
	isprimev2(n)
	#print(n, isprimev2(n))
t5 = time.time()
print("Time required v2: ",t5-t4)
def isprimev3(n):
	if n == 1:
		return False #1 is not a prime number
	if n == 2:
		return True
	if n > 2 and n % 2 == 0:
		return False
	maxdivisor = math.floor(math.sqrt(n))
	for d in range(3, 1+maxdivisor,2):
		if n % d == 0:
			return False
	return True
t6 = time.time()
for n in range(1, 11):
	print(n, isprimev3(n))
t7 = time.time()
print("Time required v3: ",t7-t2)
t8 = time.time()
for n in range(1, 100001):
	isprimev3(n)
	#print(n, isprimev3(n))
t9 = time.time()
print("Time required v3: ",t9-t8)
print("\n")

import datetime
class User:
	pass
user1 = User()
user1.firstname = "Dave"
user1.lastname = "Bowman"
print(user1.firstname) #print Dave
print(user1.lastname) #print Bowman
user2 = User()
user2.firstname = "Frank"
user2.lastname = "Poole"
print(user2.firstname) #print Frank
print(user2.lastname) #print Poole
user1.age = 37
user2.favoritebook = "2001: A Space Odyssey"
print(user1.age) #print 37
class User2:
	"""document string type print(help(user2)) for class"""
	def __init__(self, fullname, birthday):
		self.name = fullname
		self.birthday = birthday #yyymmdd
		#extract first name and last name
		namepieces = fullname.split(" ")
		self.firstname = namepieces[0]
		self.lastname = namepieces[-1]
	def age(self):
		"""Return the age of the user in years."""
		today = datetime.date(2001, 5, 12)
		yyyy = int(self.birthday[0:4])
		mm = int(self.birthday[4:6])
		dd = int(self.birthday[6:8])
		dob = datetime.date(yyyy, mm, dd) #date of birth
		print(today)
		print(dob)
		ageindays = (today - dob).days
		ageinyears = ageindays / 385
		return int(ageinyears)
user = User2("Dave Bowman","19710315")
print(user.name) #print Dave Bowman
print(user.firstname) #print Dave
print(user.lastname) #print Bowman
print(user.birthday) #print 19700315
print(user.age()) #print 28
#print(help(User2)) #press q to exit the help #RM: comment help out
print("\n")

def function(x):
	return 3*x + 1
print(function(2)) #print 7
#lambdanameexpression = lambda inputs: expressions for output
g = lambda x:3*x + 1
print(g(2)) #print 7
fullname = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(fullname(" Leonhard","euler")) #print Leonhard Euler
noinput = lambda : "What is my purpose noinput?"
print(noinput) #print <function <lambda> at 0x7fbe3f556e18>
print(noinput()) #print What is my purpose noinput?
noinput2 = lambda  x : "What is my purpose noinput2?"
print(noinput2(0)) #print What is my purpose noinput2?
geometricmean = lambda x, y:(x*y)**0.5
print(geometricmean(5,6)) #print 5.477225575051661
harmonicmean = lambda x, y, z:(1/x + 1/y + 1/z)
print(harmonicmean(4,10,12)) #print 0.4333333333333333
scifiauthors = ["Isaac Asimov","Ray Bradbury","Robert Heinlein","Arthur C. Clarke","Frank Herbert","Orson Scott Card","Douglas Adams","H.G. Wells","Leigh Brackett"]
scifiauthors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifiauthors) #print ['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H.G. Wells']
def quadraticfunction(a, b, c):
	"""return the function f(x): ax^2+bx+c"""
	return lambda x:a*x**2 + b*x + c
f = quadraticfunction(2, 3, -5)
print(f) #print <function quadraticfunction.<locals>.<lambda> at 0x7f16c58d2158>
print(quadraticfunction(3,0,1)(2)) #print 13 3x^2+0+1 for x=2
print(quadraticfunction(2,3,-5)(2)) #print 9 2*2^2+3*2+-5 for x=2

#JSON JavaScript Object Notation
#Just watched video.

earthmetals = ["Beryllium","Magnesium","Calcium","Strontium","Barium","Radium"]
print(earthmetals.sort()) #print None
sortearthmetals = earthmetals.sort()
print(sortearthmetals) #print None
earthmetals.sort()
print(earthmetals) #print ['Barium', 'Beryllium', 'Calcium', 'Magnesium', 'Radium', 'Strontium']
earthmetals.sort(reverse=True)
print(earthmetals) #print ['Strontium', 'Radium', 'Magnesium', 'Calcium', 'Beryllium', 'Barium']
#planets = (name, radius, density, distance from Sun in Astronomical Units)
planets = [("Mercury",2440,5.43,0.395),("Venus",6052,5.24,0.723),("Earth",6378,5.52,1.000),("Mars",3396,3.93,1.530),("Jupiter",71492,1.33,5.210),("Saturn",60268,0.69,9.551),("Uranus",25559,1.27,19.213),("Neptune",24764,1.64,30.070),]
size = lambda planet: planet[1]
planets.sort(key=size,reverse=True)
print(planets) #print [('Jupiter', 71492, 1.33, 5.21), ('Saturn', 60268, 0.69, 9.551), ('Uranus', 25559, 1.27, 19.213), ('Neptune', 24764, 1.64, 30.07), ('Earth', 6378, 5.52, 1.0), ('Venus', 6052, 5.24, 0.723), ('Mars', 3396, 3.93, 1.53), ('Mercury', 2440, 5.43, 0.395)]
density = lambda planet: planet[2]
planets.sort(key=density,reverse=True)
print(planets) #print [[('Earth', 6378, 5.52, 1.0), ('Mercury', 2440, 5.43, 0.395), ('Venus', 6052, 5.24, 0.723), ('Mars', 3396, 3.93, 1.53), ('Neptune', 24764, 1.64, 30.07), ('Jupiter', 71492, 1.33, 5.21), ('Uranus', 25559, 1.27, 19.213), ('Saturn', 60268, 0.69, 9.551)]]
earthmetals = ["Beryllium","Magnesium","Calcium","Strontium","Barium","Radium"]
sortedearthmetals = sorted(earthmetals)
print(sortedearthmetals) #print ['Barium', 'Beryllium', 'Calcium', 'Magnesium', 'Radium', 'Strontium']
datanumbers = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted(datanumbers)) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] convert a tuple to a list
print(datanumbers) #print (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted("Alphabetical")) #print ['A', 'a', 'a', 'b', 'c', 'e', 'h', 'i', 'l', 'l', 'p', 't']
