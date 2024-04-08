N = int(input())
S = input()

for i in range(N):
    if S[i] == 'A':
        if i+1 < N and S[i+1] == 'B':
            if i+2 < N and S[i+2] == 'C':
                print(i+1)
                exit()
print('-1')
