N,M = map(int,input().split())
s, c = [0]*M, [0]*M
for i in range(M):
    s[i], c[i] = map(int,input().split())

if N == 1:
    if M == 0:
        print(0)
    elif M == 1:
        print(c[0])        
    else:
        print(-1)
    exit()

uniq, ans = [], [0]*N
for i in range(M):
    if s[i] == 1 and c[i] == 0:
        print(-1)
        exit()
    if s[i] not in uniq:
        uniq.append(s[i])
        ans[s[i]-1] = c[i]
    else:
        if ans[s[i]-1] != c[i]:
            print(-1)
            exit()
if ans[0] == 0:
    ans[0] = 1
print(''.join(map(str,ans)).lstrip('0'))
    