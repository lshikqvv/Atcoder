N = int(input())
A = list(map(int, input().split()))

ans = []
pos = [0] * N

for i in range(N):
    A[i] -= 1
    pos[A[i]] = i

for i in range(N):
    if A[i] == i:
        continue
    j = pos[i]
    pos[A[i]], pos[A[j]] = j, i
    A[i], A[j] = A[j], A[i]
    ans.append((i+1, j+1))

print(len(ans))
for a1, a2 in ans:
    print(a1, a2)
