N,M = map(int,input().split())
A = list(map(int,input().split()))

dict = {}
max_v = 0
max_k = 0
for i in range(M):
    a = A[i]
    if a not in dict.keys():
        dict[a] = 1
    else:
        dict[a] += 1
    
    if dict[a] > max_v or (dict[a] == max_v and a < max_k):
        max_v = dict[A[i]]
        max_k = a
    print(max_k)