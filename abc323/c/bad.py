N,M = map(int,input().split())
A = list(map(int,input().split()))
S = [input() for _ in range(N)]

scr = [0]*N
for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            scr[i] += A[j]
    scr[i] += (i+1)
cap = max(scr)

B = sorted(A, reverse=True)
for i in range(N):
    ans, now = 0, scr[i]
    if now == cap:
        print(ans)
        continue
    for j in range(M):
        if now > cap: break
        L = [k for k in range(M) if A[k] == B[j]]
        for k in range(len(L)):
            if now > cap: break
            if S[i][L[k]] == 'x':
                ans += 1
                now += A[L[k]]
    print(ans)