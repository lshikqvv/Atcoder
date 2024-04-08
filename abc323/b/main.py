N = int(input())
S = [input() for _ in range(N)]

W = [0]*N
for i in range(N):
    for s in S[i]:
        if s == 'o':
            W[i] += 1

for i in range(N,-1,-1):
    l = [j for j in range(N) if W[j] == i]
    if len(l) == 0: continue
    if len(l) == 1:
        print(l[0]+1, end=' ')
    else:
        # cnt = [0]*len(l)
        # for j in range(len(l)):
        #     for k in range(len(l)):
        #         if S[l[j]][k] == 'o':
        #             cnt[j] += 1
        # nom = sorted(cnt, reverse=True)       
        # for n in nom:
        #     print(l[cnt.index(n)]+1, end=' ')
        for n in l:
            print(n+1, end=' ')
                
