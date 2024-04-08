N,K,M = map(int,input().split())
A = list(map(int, input().split()))

n = N*M - sum(A)
if n > K:
    print(-1)
else:
    print(max(0,n))
