#Socratica 002 Hello world, 003 Introduction to Strings, 004 Numbers in Version 2, 005 Numbers in Version 3, 006 Arithmetic in Python V2, 007 Arithmetic in Python V3, 009 Booleans, 010 If then else, 011 Python Functions, 

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
