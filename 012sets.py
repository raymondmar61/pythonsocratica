#each item inside a set is called an element.  No duplicates in a set.
example = set()
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
print(example) #returns {False, 42, 3.14159, 'Thorium'}.  Order return is random.  Order doesn't matter
print(len(example)) #returns 4
example.remove(42)
print(example)
example.discard(50) #discard method doesn't display an error message if the element to be discarded is not in the set.  50 is not in an element.  No error.  Nothing happens.
print(example)

example2 = set([28, True, 2.71827, "Helium"])
print(example2)
print(len(example2))
example2.clear() #removes all elements
print(len(example2))

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])
print(odds.union(evens))
print(odds)
print(evens)
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds)) #no numbers.  Return set()
print(primes.union(composites))
print(2 in primes) #returns True
print(6 in odds) #returns False
print(9 not in evens) #returns True
