import collections as cl

N = int(input())
S = input()
C = S.count('0')
tmp = cl.Counter(S)

if tmp['0'] == N:
    print(1)
    exit()
ans = 0

for i in range(C + 1):
    n = N - i

    top = 1
    while top * top < 10 ** (n-1):
        top += 1

    end = 1
    while end * end < 10 ** n:
        end += 1

    for j in range(top, end):
        chr = cl.Counter(str(j * j))
        if tmp == chr:
            ans += 1

    if i < C:
        tmp['0'] -= 1

print(ans)
