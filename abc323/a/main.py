S = input()
for i in range(1,len(S)):
    if i%2 != 0:
        if S[i] != '0':
            # print(i)
            # print(S[i])
            print('No')
            exit()
print('Yes')