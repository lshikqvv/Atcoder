N,X,Y = map(int,input().split())

ans = [0] * N
for i in range(1,N+1):
    for j in range(i+1,N+1):
        ans[min(j-i,abs(X-i)+1+abs(Y-j))] += 1
print(*ans[1:],sep="\n")