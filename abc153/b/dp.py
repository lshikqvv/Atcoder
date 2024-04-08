H,N = map(int,input().split())
A = list(map(int,input().split()))

if sum(A) > H:
    print('No')
else:
    dp = [[0]*(H+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(H+1):
        for j in range(N):
            if dp[j][i] == 1:
                dp[j+1][i] = 1
                if i+A[j] <= H:
                    dp[j+1][i+A[j]] = 1
    if dp[N][H] == 1:
        print('Yes')
    else:
        print('No')


