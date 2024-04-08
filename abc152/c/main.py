N = int(input())
P = list(map(int,input().split()))

min, cnt = N+1, 0
for i in range(N):
    if P[i] <= min:
        min = P[i]
        cnt += 1
print(cnt)