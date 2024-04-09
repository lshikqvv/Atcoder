N = int(input())
S = input()

if N == 1:
    print(-1)
    exit()

if 'o' not in S:
    print(-1)
    exit()

max, cnt = -1, 0
old = ''
for s in S:
    if s == '-':
        max = max if max > cnt else cnt
        cnt = 0
    else:
        cnt += 1

    old = s

T = S[::-1]
cnt = 0
old = ''
for t in T:
    if t == '-':
        max = max if max > cnt else cnt
        cnt = 0
    else:
        cnt += 1

    old = t

print(max)
