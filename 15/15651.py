n,m=map(int,input().split())

arr=[]

def solve(depth,n,m):
    if(depth==m):
        print(' '.join(map(str,arr)))
        return

    for i in range(n):
        arr.append(i+1)
        solve(depth+1,n,m)
        arr.pop()





solve(0,n,m)