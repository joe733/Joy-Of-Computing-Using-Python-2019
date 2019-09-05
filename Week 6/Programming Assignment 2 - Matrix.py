x, y = map(int, input().split())
for i in range(1,x*y+1):
  if i < x*y:
    print(i, end="\n" if i%y == 0 else " ")
print(i, end="")