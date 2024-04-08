N = int(input())
A = list(map(int,input().split()))

a = max(A)
A = [i for i in A if i != a]
print(max(A))
