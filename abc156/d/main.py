n,a,b = map(int,input().split())
mod = 10**9+7

def comb(r):
    top, btm = 1, 1
    for i in range(r):
        top *= (n-i)
        btm *= (i+1)
        top %= mod
        btm %= mod
    return int(top * pow(btm, mod-2, mod))

print((pow(2,n,mod)-1-comb(a)-comb(b))%mod)


        