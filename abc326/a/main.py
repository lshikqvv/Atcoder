X,Y = map(int,input().split())

if X > Y:
    if X-Y <= 3:
        print("Yes")
    else:
        print("No")
else:
    if Y-X <= 2:
        print("Yes")
    else:
        print("No")