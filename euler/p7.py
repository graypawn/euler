import math
import itertools as it

def isPrime(n):
    return all(map(lambda x:n%x!=0,list(range(3,int(math.sqrt(n))+1,2))))

def question(n):
    return next(it.islice(filter(isPrime,it.count(3,2)),n-2,None))

print(question(10001))
