primes = [2, 3, 5, 7, 11, 13]
print(primes)
primes.append(17)
primes.append(19)
print(primes)
print(primes[1])
print(primes[-1]) #returns 19.  Python wraps around the list.  primes[0] is 2, primes[-1] is 19 which wraps to the right side of the list

primes = [2, 3, 5, 7, 11, 13, 17, 19]
print(primes[2:5]) #we are slicing.  Returns [5, 7, 11].  Slice.

numbers = [1, 2, 3]
letters = ["a","b","c"]
print(numbers + letters) #returns [1, 2, 3, 'a', 'b', 'c'].  Concatenate lists.

