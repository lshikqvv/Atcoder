N = int(input())
S = input()

flg = False
for s in S:
    if flg:
        if s == '*':
            print('in')
            exit()
        elif s == '|':
            print('out')
            exit()
    elif s == '|':
        flg = True
