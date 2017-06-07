def f(): #inside paranthesis are the inputs or arguments.  Can be blank.
	pass

def ping():
	return "Ping!" #functions can return values.  Type return and the object to return a value.  return values are optional.
print(ping())

#volume of a sphere is V = (4/3)(pi)(r*r*r)
import math
print(math.pi)
def volume(radius):
	"""Returns the volume of a sphere with radius r."""
	volume = (4/3)*(math.pi)*(radius**3)
	return volume
print(volume(2))
#print(help(volume)) #returns the """ statement in volume(radius):

def trianglearea(base, height):
	"""Returns the area of a triangle with base and height."""
	return 0.5 * base * height
print(trianglearea(3, 6))

#keyword arguments.  Assign a default value to the arguments
def cm(feet = 0, inches = 0):
	"""Converts a length from feet and inches to centimeters."""
	inchestocm = inches * 2.54
	feettocm = feet * 12 * 2.54
	return inchestocm + feettocm
print(cm(feet = 5))
print(cm(inches = 70))
print(cm(feet = 5, inches = 8))
print(cm(inches = 8, feet = 5))

#There are two types of function arguments:  keyword and required.  Keyword arguments have the equal sign.  Required arguments must come first.
def g(requiredargument, keywordargument = 17):
	print(requiredargument, keywordargument)
g(5)
g(9,90)