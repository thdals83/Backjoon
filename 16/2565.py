x=int(input())

arr=[]
arr2=[]
dp=[0 for _ in range(x)]

for i in range(x):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:x[0])

for i in range(x):
    arr2.append(arr[i][1])

for i in range(x):
    for j in range(i):
        if arr2[i]>arr2[j] and dp[i]<dp[j]:
            dp[i]=dp[j]

    dp[i]=dp[i]+1

print(x-max(dp))