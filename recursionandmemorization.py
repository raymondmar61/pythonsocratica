#write a function to return the nth term of Fibonacci Sequence

def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))

def fibonacciforloop(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacciforloop(n-1) + fibonacciforloop(n-2)
for n in range(1,11):
	print(n, ":", fibonacciforloop(n), "going too slow.  Need Memorization.")

#Memorization is store the values for recent function calls so future calls don't have to repeat the work.  There are several ways:  implement explicitly and use built-in python tool "from functools import lru_cache".

#create a dictionary fibonacci_cache which stores recent function calls.
fibonacci_cache = {}
print(fibonacci_cache)
def fibonaccicache(n):
	#if we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	# Compute the Nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 2
	elif n > 2:
		value = fibonaccicache(n-1) + fibonaccicache(n-2)
	#Cache the value in fibonacci_cache dictionary and return it
	fibonacci_cache[n] = value
	return value
for n in range(1,101):
	print(n, ":", fibonaccicache(n), "going faster use memorization.")
	print(fibonacci_cache)

#Clean approach using LeaseRecentlyUsed_Cache lru_cache provides a one line way to add memorization

from functools import lru_cache
#enter number of values to lru_cache in maxsize
@lru_cache(maxsize = 1000)
def fibonaccilrc(n):
	if type(n) != int:
		raise TypeError("n must be a positive int")
	if n < 1:
		raise ValueError("n must be a positive int")
	if n == 0:
		return 0
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonaccilrc(n-1) + fibonaccilrc(n-2)
for n in range(1,501):
	print(n, ":", fibonaccilrc(n), "Use lru_cache.")