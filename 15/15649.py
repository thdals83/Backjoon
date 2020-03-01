n,m=map(int,input().split())

visited=[False]*n
arr=[]

def solve(depth,n,m):
    if(depth==m):
        print(' '.join(map(str,arr)))
        return

    for i in range(n):
        if(visited[i]==False):
            visited[i]=True
            arr.append(i+1)
            solve(depth+1,n,m)
            visited[i]=False
            arr.pop()

solve(0,n,m)


'''
from itertools import permutations
N, M = map(int, input().split())

P = permutations(range(1, N+1), M)  # iter(tuple)
for i in P:
    print(' '.join(map(str, i)))  # tuple -> str
'''
