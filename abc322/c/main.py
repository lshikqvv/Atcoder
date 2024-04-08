N,M = map(int,input().split())
A = list(map(int,input().split()))

B = [0] * (N+1)
for i in range(M):
    B[A[i]] = 1

i = 1
while i < N+1:
    for j in range(i,N+1):
        if B[j]:
            for k in range(j-i,-1,-1):
                print(k)
            i = j+1
            break
    
