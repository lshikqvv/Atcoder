N = int(input())
S = input()

A = set(S)
k = len(A)
ans = 0

if k == 1:
    print(N)
    exit()

for a in A:
    cnt = 2
    while a * cnt in S:
        cnt += 1
        ans += 1
print(ans + k)
