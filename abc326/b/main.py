n = int(input())

while True:
    S = str(n)
    a = int(S[0])
    b = int(S[1])
    c = int(S[2])

    if a*b == c:
        print(n)
        exit()
    n += 1
