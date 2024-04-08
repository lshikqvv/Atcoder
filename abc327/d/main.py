N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_match(x):
    for i in range(M):
        a = (x >> A[i]) & 1
        b = (x >> B[i]) & 1
        if a == b:
            return 0
    return 1

for i in range(M):
    if A[i] == B[i]:
        print('No')
        exit()

for x in range(2**N):
    if is_match(x):
        print('Yes')
        exit()
print('No')
