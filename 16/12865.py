import sys

(N,K) = map(int,sys.stdin.readline().split())

arr=[[0,0]]
for i in range(1,N+1):
    arr.append(list(map(int,sys.stdin.readline().split())))

dp=[[0]* (K+1) for _ in range(N+1)]


for i in range(1,N+1):
    for j in range(1,K+1):
        if j>= arr[i][0]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-arr[i][0]]+arr[i][1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[N][K])
