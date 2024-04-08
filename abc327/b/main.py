B = int(input())

ans = 1
while True:
    if ans ** ans == B:
        print(ans)
        break
    elif ans ** ans > B:
        print(-1)
        break
    else:
        ans += 1