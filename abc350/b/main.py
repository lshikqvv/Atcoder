N,Q = map(int,input().split())
T = list(map(int,input().split()))

H = [1] * N
for t in T:
    if H[t-1]:
        H[t-1] = 0
    else:
        H[t-1] = 1

print(sum(H))
