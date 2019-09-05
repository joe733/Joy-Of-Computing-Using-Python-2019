from random import randint
n=int(input())
x = [int(input()) for i in range(n)]
while True:
    i, j = randint(0,n-1), randint(0,n-1)
    x[i], x[j] = x[j], x[i]
    if all(x[i] <= x[i+1] for i in range(len(x)-1)): break
[print(x[i], end=" " if i <len(x)-1 else "") for i in range(len(x))]