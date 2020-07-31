tmp =[0]*200

def dp(n):
    if (n==1): return 1
    if (n==2): return 1
    if (n==3): return 1
    if(tmp[n]!=0): return tmp[n]
    y=dp(n-3)+dp(n-2)
    tmp[n]=y
    return tmp[n]

if __name__=="__main__":
    x=int(input())

    for _ in range(x):
        y=int(input())
        print(dp(y))

