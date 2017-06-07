#data ordered in a sequence in a tuple is smaller in memory and faster to create surrounded by parenthesis.
#lists.  Add, remove, change data.
#tuple.  Can't be changed.  Immutable.

listprimenumbers = [2, 3, 5, 7, 11, 13, 17]
tupleperfectsquares = [1, 4, 9, 16, 25, 36]

print(len(listprimenumbers)) #returns 7
print(len(tupleperfectsquares)) #returns 6
for eachlistprimenumbers in listprimenumbers:
	print("Prime:",eachlistprimenumbers)
for eachtupleperfectsquares in tupleperfectsquares:
	print("Perfect square:",eachtupleperfectsquares)

emptytuple = ()
test1 = ("a")
test1b = ("a",) #need a comma to return "a" as a tuple
test2 = ("a","b")
test3 = ("a","b","c")
print(emptytuple)
print(test1) #returns a.  not ('a')
print(test1b) #returns ('a',).
print(test2)
print(test3)

#tuple assignment
#(age, country, knows_python)
survey = (27, "Vietnam", True)
age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age =", age)
print("Country =", country) #notice comma instead of plus sign.  country is string.
print("Knows Python?", knows_python)

#(age, country, knows_python)
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age =", age)
print("Country =", country) #notice comma instead of plus sign.  country is string.
print("Knows Python?", knows_python)