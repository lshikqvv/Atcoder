A = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    if len(A[i]) != len(set(A[i])):
        print('No')
        exit()
    for j in range(9):
        col = [A[i][j] for i in range(9)]
        if len(col) != len(set(col)):
            print('No')
            exit()

for i in range(3):
    for j in range(3):
        blk = []
        for k in range(3):
            for l in range(3):
                blk.append(A[i*3+k][j*3+l])
        if len(blk) != len(set(blk)):
            print('No')
            exit()

print('Yes')

