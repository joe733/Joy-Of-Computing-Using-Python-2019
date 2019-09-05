N=int(input())
A = list(map(int, input().split()))
[print((str(A[i]+A[::-1][i])+" " if i<N-1 else A[i]+A[::-1][i]), end="") for i in range(N)]