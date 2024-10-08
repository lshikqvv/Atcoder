from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N):
    ans = max(ans, bisect_left(A, A[i]+M) - i)
print(ans)
