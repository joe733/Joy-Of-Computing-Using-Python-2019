def printDict():
  print(dict([(i,i**2) for i in range (1,x+1)]), end="")
x=int(input())
printDict()