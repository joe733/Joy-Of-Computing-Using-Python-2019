#N = distance in m
# V1 = Arun's Velocity
# V2 = Cab's Velocity <<but somthing is wrong with the examples>>
from math import sqrt
x = list(map(int, input().split()))
t1 = x[0]*sqrt(2)*x[1]
t2 = x[0]*x[2]
print("Walk" if t1 > t2 else "Cab", end="")