x, y = map(int, input().split())
z = [list(map(int, input().split())) for i in range(x)]
print("YES" if all(all(j<=1 for j in i) for i in z) else "NO", end="")