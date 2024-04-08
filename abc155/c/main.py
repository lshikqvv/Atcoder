import collections as c

N = int(input())
S = [input() for _ in range(N)]
cnt = c.Counter(S)
max = max(cnt.values())

ans = [k for k, v in cnt.items() if v == max]
ans.sort()
print(*ans, sep='\n')

