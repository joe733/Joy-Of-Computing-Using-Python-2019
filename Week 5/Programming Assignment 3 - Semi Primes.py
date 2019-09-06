'''
 A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).

>>Input Format:
The first line contains an integer N.

>>Output Format:
Print 'Yes' if it is possible to represent N as a sum of two semiprimes 'No' otherwise.

>>Example:

Input:
30

Output:
Yes

>>Explanation:
N = 30 can be expressed as 15+15 where 15 is a semi-prime number (5*3 = 15)

NOTE: N is less than equal to 200 
'''
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
