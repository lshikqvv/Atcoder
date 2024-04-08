N = int(input())
X = list(map(int,input().split()))
X.sort()
p, min = X[0], 10**9
while True:
    sum = 0
    for i in range(N):
        sum += (X[i]-p)**2
    if sum <= min:
        min = sum
    else:
        print(min)
        exit()
    p += 1
    