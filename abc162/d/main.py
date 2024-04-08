# import collections as cl
# import math as mt

N = int(input())
S = input()

# cnt = cl.Counter(S)
# ans = mt.prod(cnt.values())
ans = S.count("R") * S.count("G") * S.count("B")

for i in range(N):
    _i = S[i]
    for j in range(i+1, N):
        _j = S[j]
        if _i != _j:
            k = 2*j - i
            if k < N and _i != S[k] and _j != S[k]:
                ans -= 1
print(ans)
