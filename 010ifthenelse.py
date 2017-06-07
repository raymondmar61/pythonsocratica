userinput = input("Please enter a test string: ")
if len(userinput) < 6:
	print("Your string is too short.\nPlease enter a string with at least 6 characters.")
#I really didn't need an else statement for len(userinput) >=6:

number = int(input("Please enter an integer: "))
if number % 2 == 0:
	print("Your number is even.")
else:
	print("Your number is odd.")

#Scalene triangle all sides different lengths
#Isosceles triangle two sides are the same lenghts
#Equilateral triangle all sides are the same
a = int(input("The length of triangle side a = "))
b = int(input("The length of triangle side b = "))
c = int(input("The length of triangle side c = "))
if a != b and b != c and a != c:
	print("This is a scalene triangle.")
elif a == b and b ==c:
	print("This is an equilateral triangle.")
else:
	print("This is an isosceles triangle")