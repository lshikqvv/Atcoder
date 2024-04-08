N,A = map(int,input().split())

q = N//A
if N%A == 0:
    print(q)
else:
    print(q+1)