x= int(input())
arr=list(map(int,input().split()))

dp=[0 for _ in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i]>arr[j] and dp[i]<dp[j]:
            dp[i]=dp[j]

    dp[i]=dp[i]+1

print(max(dp))