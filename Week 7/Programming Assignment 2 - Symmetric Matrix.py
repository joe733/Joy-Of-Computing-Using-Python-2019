z, l = [], []
n = int(input())
[z.append(list(map(int, input().split()))) for i in range(n)]
[l.append(list(i)) for i in list(zip(*z))]
print ("YES" if l == z else "NO", end="")