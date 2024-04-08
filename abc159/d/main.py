import collections as cl

def combination(n):
    return n*(n-1)//2

N = int(input())
A = list(map(int,input().split()))

c = cl.Counter(A)
nom = {}
for k,v in c.items():
    if v >= 2:
        nom.update({k:combination(v)})
    else:
        nom.update({k:0})

sum = sum(nom.values())
for a in A:
    ans = sum - nom[a] + combination(c[a]-1)
    print(ans)


    
