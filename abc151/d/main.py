from collections import deque

H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]

ans = 0
mv = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#': continue
        dist = [[-1]*W for _ in range(H)]
        dist[i][j] = 0
        que = deque([(i,j)])
        while que:
            h,w = que.popleft()
            for dh, dw in mv:
                nh, nw = h+dh, w+dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W: continue
                if S[nh][nw] == '#' or dist[nh][nw] != -1 : continue
                dist[nh][nw] = dist[h][w] + 1
                que.append((nh,nw))
        ans = max(ans, max([max(d) for d in dist]))
print(ans)


