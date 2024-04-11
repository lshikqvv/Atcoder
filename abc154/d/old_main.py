N,K = map(int,input().split())
p = list(map(int,input().split()))
E = [(1+p[i])/2 for i in range(N)]

sum = sum(E[:K])
ans = sum
for i in range(N-K):
    sum = sum-E[i]+E[i+K]
    ans = max(sum, ans)
print(ans)