tmp=[0]*1000000

def dp(x):
    if(x==0): return 0
    if(x==1): return 1
    if(tmp[x]!=0): return tmp[x]
    y=dp(x - 1) + dp(x - 2)
    print(dp(x - 1))
    print(dp(x - 2))
    print("체크")
    tmp[x] = y
    return tmp[x]

if __name__=="__main__":
    x=int(input())
    print(dp(x))

'''
n=int(input())
m={0:0, 1:1}
def f(n):
    if n not in m: m[n] = f(n-1)+f(n-2)
    return m[n]
print(f(n))
'''