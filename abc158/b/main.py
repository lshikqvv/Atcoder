N,A,B = map(int,input().split())
c = N // (A+B)
r = N % (A+B)

print(c*A + min(r,A))