N,M = map(int,input().split())

if N == 0:
    print(M*(M-1)//2)
elif N == 1:
    print(0)
else:
    print(N*(N-1)//2 + M*(M-1)//2)