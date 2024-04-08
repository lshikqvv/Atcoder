N = int(input())
A = list(map(int,input().split()))

d = A[0]
for a in A:
    if a !=  d:
        print("No")
        exit()
print("Yes")