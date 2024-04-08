N,M = map(int,input().split())

P, S = [], []
for i in range(M):
    p, s = input().split()
    P.append(int(p))
    S.append(1 if s == 'AC' else 0)

AC, WA = [0]*N, [0]*N
for i in range(M):
    if S[i] == 1:
        AC[P[i]-1] = 1
    else:
        if AC[P[i]-1] == 0:
            WA[P[i]-1] += 1
print(sum(AC), sum([AC[i]*WA[i] for i in range(N)]))
