A = list(map(int, input().split()))
[print(A[i], end="" if i==len(A)-1 else " ") for i in range(len(A)) if not A[i]%5]