import itertools as it
import euler.p7 as p7

def question(n):
    return sum(filter(p7.isPrime,[2]+list(range(3,n+1,2))))
