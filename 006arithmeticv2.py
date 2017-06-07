#Run the python program in version 2.7
#Four times of numbers:  int, long, float, complex
x = 5
y = 5L
print(x)
print(y)
x = 28L
y = 28.0
print(x)
print(y)
pie = 3.14
print(pie)
print(long(pie)) #returns 3, doesn't return 3L
x = 1.732 #float
print(x)
x = 1.732 + 0j #add 0j to convert a float to a complex
print(x) #returns (1.732 + 0j)
print("\n")

a = 2 #int
b = 3L #long
c = 6.0 #float
d = 12 + 0j #complex
print(a + b) #tutorial returned 5L.  I returned 5
print(c - b) #returns 3.0
print(a * c) #returns 12.0
print(d / c) #(2+0j)
print("\n")

print(16/5) #returns 3.  Divide an integer by an integer returns an integer
print(16 % 5) #returns 1
print(float(16)/5) #returns 3.2
print(16/float(5)) #returns 3.2
print(16.0/5) #returns 3.2
