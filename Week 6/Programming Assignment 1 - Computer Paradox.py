x = int(input()) #Actually not needed...
y = list(map(int, input().split()))
z = int(input())
print(sorted(y).index(y[z-1])+1, end="")