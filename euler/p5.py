from functools import reduce
import math

def question(n):
    return reduce(lambda x,y:(x*y)//math.gcd(x,y),range(1,n+1))

print(question(20))
