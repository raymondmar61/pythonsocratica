#Run the python program in version 3
#Three times of numbers:  int, float, complex

x = 28
y = 28.0
print(x)
print(y)
print(float(x))
x = 1.732 #float
print(x)
print(complex(x)) #convert a number to complex use complex()
x = 1.732 + 0j #add 0j to convert a float to a complex
print(x) #returns (1.732 + 0j)
print("\n")

a = 2 #integer
b = 6.0 #float
c = 12 + 0j #complex
print(a + b) #returns 8.0 float
print(b - a) #returns 4.0 float
print(a * 7) #returns 14 integer
print(c / b) #returns (2+0j) complex
print("\n")

print(16 / 5) #returns 3.2 float (FYI python2.7 returns 3)
print(20 / 5) #returns 4.0 float
print(16 % 5) #returns 1 remainder
print(16 // 5) #returns quotient 3