A,B = map(int,input().split())

a = int(A//0.08)
ans = []

if int(0.08*a) == A:
        if int(0.1*a) == B:
            ans.append(a)
a += 1
while True:
    if int(0.08*a) == A:
        if int(0.1*a) == B:
            ans.append(a)
    else: break
    a += 1
print(min(ans) if len(ans) > 0 else -1)

        