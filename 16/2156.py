x=int(input())


arr=[0 for _ in range(x+1)]
dp=[0 for _ in range(x+1)]
arr[0]=0
dp[0]=0
for i in range(1,x+1):
    arr[i]=int(input())


dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(arr[1]+arr[2],arr[1]+arr[3],arr[2]+arr[3])
for i in range(3,x+1):
    dp[i]=max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])


print(dp[x])