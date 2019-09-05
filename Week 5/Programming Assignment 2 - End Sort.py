x = list(map(int, input().split()))
y = x.copy()
x.sort()
k = 0
for i,j in zip(x, x[1:]):
    if x == y:
        break
    if y.index(i) > y.index(j) and i<j:
        y.append(y.pop(y.index(j)))
        k+=1
print(k,end="")