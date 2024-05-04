from collections import deque

N,M = map(int,input().split())
G = {set(i) for i in range(N)}
for i in range(M):
    a, b = map(int,input().split())
    G[a-1].add(b-1)
    G[b-1].add(a-1)

que = deque([0])

dist = [-1]*N
dist[0] = 0

while que:
    v = que.popleft()
    for u in G[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            que.append(u)

