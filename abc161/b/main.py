N,M = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)
std = sum(A)/(4*M)
if A[M-1] >= std:
    print("Yes")
else:
    print("No")