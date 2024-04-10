N = int(input())

lt, rt = 1, N
while lt + 1 != rt:
    md = (rt + lt) // 2
    print('?', md)
    s = int(input())
    if s == 0:
        lt = md
    else:
        rt = md
print('!', lt)
