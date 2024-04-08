N = int(input())
cnt = [[0] * 10 for _ in range(10)]

for i in range(1, N+1):
    top, btm = int(str(i)[0]), i%10
    cnt[top][btm] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]
print(ans)
        