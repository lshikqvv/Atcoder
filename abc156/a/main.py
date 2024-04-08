N,R = map(int,input().split())

ans = R if N >= 10 else R + 100 * (10 - N)

print(ans)