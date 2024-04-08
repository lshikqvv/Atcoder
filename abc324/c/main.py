N, T = map(str, input().split())
N = int(N)

k, ans = 0, []
for i in range(N):
    flg, idx = 0, 0
    S = input()
    siz = len(S) - len(T)
    if siz == 0:
        for j in range(len(S)):
            if j < len(S) - 1:
                if S[j] == T[j]:  pass
                elif flg == 0:
                    flg = 1
                else:  break
            else:
                if S[j] == T[j] or flg == 0:
                    k += 1
                    ans.append(i+1)
                else:  break
    elif siz == 1:
        for j in range(len(T)):
            if j != len(T) - 1:
                if S[idx] == T[j]:  pass
                elif flg == 0:
                    flg = 1
                    if S[idx+1] == T[j]:
                        idx += 1
                    else: break
                else:  break
                idx += 1
            else:
                if S[idx] == T[j]:
                    k += 1
                    ans.append(i+1)
                elif flg == 0:
                    flg = 1
                    if S[idx+1] == T[j]:
                        k += 1
                        ans.append(i+1)
                    else: break
                else:  break
    elif siz == -1:
        for j in range(len(S)):
            if j != len(S) - 1:
                if S[j] == T[idx]:  pass
                elif flg == 0:
                    flg = 1
                    if S[j] == T[idx+1]:
                        idx += 1
                    else: break
                else:  break
                idx += 1
            else:
                if S[j] == T[idx]:
                    k += 1
                    ans.append(i+1)
                elif flg == 0:
                    flg = 1
                    if S[j] == T[idx+1]:
                        k += 1
                        ans.append(i+1)
                    else: break
                else:  break
print(k)
print(*ans)

