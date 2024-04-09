N,T = map(int,input().split())

C = list(map(int,input().split()))
R = list(map(int,input().split()))

max = -1
for i in range(N):
    if C[i] == T:
        if max < R[i]:
            num, max = i+1, R[i]

if max < 0:
    num, max = 1, R[0]
    for i in range(1,N):
        if C[i] == C[0]:
            if max < R[i]:
                num, max = i+1, R[i]

print(num)
