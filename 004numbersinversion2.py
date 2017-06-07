#Run the python program in version 2.7
#Four times of numbers:  int, long, float, complex
a = 28
print(a)
print(type(a))
c = 2147483648
print(c)
print(type(c)) #didn't say c is <type 'long'>
f = 1L
print(f)
print(type(f)) #did say f is <type 'long'> adding "L" at the end of f = 1L.  Interesting
e = 2.718281828
print(e)
print(type(e))
z = 3 + 5.7j #j converts 5.7 to an imaginary number
print(z)
print(type(z))
print(z.real) #returns 3.0
print(z.imag) #returns 5.7
