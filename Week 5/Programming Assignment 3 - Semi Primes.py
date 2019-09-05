from functools import reduce
def genPrime(n):
    return [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]

def genSemiPrime(plst):
	return list(set([x*y for x in plst for y in plst if x != y]))

def genSumOfSemiPrime(splst):
	return list(set([x+y for x in splst for y in splst if x != y]))

x = int(input())
primeList = genPrime(x)
semiPrime = genSemiPrime(primeList)
gSumSemiPrime = genSumOfSemiPrime(semiPrime)
print("Yes" if x in gSumSemiPrime else "No",end="")