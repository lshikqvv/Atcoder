def count_board(input_board):
    rows = len(input_board)
    cols = len(input_board[0])
    num = 0
    for i in range(rows):
        for j in range(cols):
            if input_board[i][j] == '#':
                num += 1
    return num

def shift_board(input_board):
    rows = len(input_board)
    cols = len(input_board[0])
    
    patterns = []
    num = count_board(input_board)

    for i in range(4):  # 四方向に平行移動するために4回繰り返す
        for r in range(4):
            for c in range(4):
                shifted_board = [['.' for _ in range(4)] for _ in range(4)]

                for x in range(rows):
                    for y in range(cols):
                        if i == 0:  # 左に平行移動
                            if y + c < 4 and x + r < 4:
                                shifted_board[x + r][y + c] = input_board[x][y]
                        elif i == 1:  # 上に平行移動
                            if x + r < 4 and y + c < 4:
                                shifted_board[x + r][y + c] = input_board[x][y]
                        elif i == 2:  # 右に平行移動
                            if x + r < 4 and y - c >= 0:
                                shifted_board[x + r][y - c] = input_board[x][y]
                        else:  # 下に平行移動
                            if x - r >= 0 and y + c < 4:
                                shifted_board[x - r][y + c] = input_board[x][y]

                if num == count_board(shifted_board):
                    patterns.append(shifted_board)
                    # for a in shifted_board:
                    #     print(*a)
                    #     print()
                    # print()

    return patterns

def rotate(board, n):
    def rotate_clockwise(board):
        return list(map(list, zip(*board[::-1])))

    rotation = []

    # 初期の盤面を追加
    rotation.append(board)

    # 90度ずつ回転させた盤面を追加
    for _ in range(n):
        board = rotate_clockwise(board)
        rotation.append(board)

    return rotation

def remove_dot_rows_and_columns(input_board):
    # 行と列の数を取得
    num_rows = len(input_board)
    num_cols = len(input_board[0]) if num_rows > 0 else 0

    # '.'のみで構成される行を特定
    rows_to_remove = []
    for i in range(num_rows):
        if all(cell == '.' for cell in input_board[i]):
            rows_to_remove.append(i)

    # '.'のみで構成される列を特定
    cols_to_remove = []
    for j in range(num_cols):
        if all(input_board[i][j] == '.' for i in range(num_rows)):
            cols_to_remove.append(j)

    # 行と列を削除して新しい行列を作成
    result_matrix = [
        [input_board[i][j] for j in range(num_cols) if j not in cols_to_remove]
        for i in range(num_rows) if i not in rows_to_remove
    ]

    return result_matrix

def trans_board(board):
    X = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == '#':
                idx = str(i) + str(j)
                sft = int(idx, 4)
                X =  X | (1<<sft)
    return X

A = [list(input()) for _ in range(4)]
B = [list(input()) for _ in range(4)]
C = [list(input()) for _ in range(4)]

def trans(input_board):
    board = remove_dot_rows_and_columns(input_board)
    patterns = rotate(board, len(board))

    result, res = [], []
    for pattern in patterns:
        result += shift_board(pattern)

    for pattern in result:
        pattern = int(format(trans_board(pattern), '016b'),2)
        res.append(pattern)

    return res

# trans_B = trans(B)
# for b in trans_B:
#     print(*b, sep='\n')
#     print()

trans_A = list(set(trans(A)))
trans_B = list(set(trans(B)))
trans_C = list(set(trans(C)))

for a in trans_A:
    for b in trans_B:
        ab = a^b
        if a&b != 0:
            continue
        for c in trans_C:
            if ab^c == 65535:
                print('Yes')
                exit()
print('No')
