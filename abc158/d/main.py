from collections import deque

S = deque(input())
Q = int(input())

flg = 0
for i in range(Q):
    que = input().split()
    if que[0] == "1":
        flg = 1 - flg
    else:
        f = int(que[1]) - 1
        c = que[2]
        if f == flg:
            S.appendleft(c)
        else:
            S.append(c)

print("".join(S) if flg == 0 else "".join(S)[::-1])
