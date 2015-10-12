import math
import itertools as it

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(it.islice(iterable, n, None), default)

def prime():
    yield 2
    def isPrime(n):
        return all(map(lambda x:n%x!=0,range(2,int(math.sqrt(n))+1)))
    for i in filter(isPrime,it.count(3,2)):
        yield i

def question(n):
    return next(it.islice(prime(),n-1,None))

print(question(10001))
