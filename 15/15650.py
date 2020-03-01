N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
arr = []  # 출력 내용

def solve(depth,idx, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, arr)))
        return
    for i in range(idx,N):
        if visited[i]==False:
            visited[i] = True
            arr.append(i + 1)
            solve(depth+1,idx+1, N, M)
            visited[i] = False
            arr.pop()

solve(0,0, N, M)



"""1
from itertools import combinations
N, M = map(int, input().split())

P = combinations(range(1, N+1), M)  # iter(tuple)
for i in P:
    print(' '.join(map(str, i)))  # tuple -> str
"""
