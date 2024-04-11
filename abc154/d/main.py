N, K = map(int, input().split())
P = list(map(int, input().split()))

s = [0] * (N + 1)
for i in range(N):
    s[i+1] = s[i] + P[i]

max = -1
for i in range(N - K + 1):
    sum = s[i + K] - s[i]
    if sum > max:
        max = sum

print((max + K) / 2)
