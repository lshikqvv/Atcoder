D = int(input())
N = int(input())

dif = [0] * (D+2)
for i in range(N):
    L ,R = map(int, input().split())
    dif[L] += 1
    dif[R+1] -= 1

ans = 0
for i in range(1, D+1):
    ans += dif[i]
    print(ans)
