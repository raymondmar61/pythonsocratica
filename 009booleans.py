#Boolean values:  True, False.  Two values.  T in True and F in False are capitalized.
a = 3
b = 5
print(a == b) #returns False
print(a != b) #returns True
print(a > b) #returns False
print(a < b) #returns True
print(type(a < b)) #returns <class 'bool'>
print(type(True)) #returns <class 'bool'>
print("\n")

print(bool(28))
print(bool(-2.71828))
print(bool(0)) #returns False
print(bool("Turing"))
print(bool(" "))
print(bool("")) #returns False
print("\n")

print(int(True)) #returns 1
print(int(False)) #returns 0
print(5 + True) #returns 6
print(10 * False) #returns 0