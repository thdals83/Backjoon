n,m=map(int,input().split())


visited=[False]*n
arr=[]

def solve(depth,n,m):
    if(depth==m):
        print(' '.join(map(str,arr)))
        return

    for i in range(n):
        if(visited[i]==False):
            for j in range(i-1,-1,-1):
                visited[j]=True
            arr.append(i + 1)
            solve(depth + 1, n, m)
            for j in range(i-1,-1,-1):
                visited[j]=False
            arr.pop()

solve(0,n,m)

'''
import itertools

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
    
for num in itertools.combinations_with_replacement(num_list, M):
    for i in num:
        print(i, end = ' ')
    print(end = '\n')
'''