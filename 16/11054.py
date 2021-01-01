x= int(input())
arr=list(map(int,input().split()))

increase=[0 for _ in range(x)]
decrease=[0 for _ in range(x)]
dp=[0 for _ in range(x)]

for i in range(x):
    for j in range(x):
        if arr[i]>arr[j] and increase[i]<increase[j]:
            increase[i] = increase[j]
    increase[i]=increase[i]+1


for i in range(x-1,-1,-1):
    for j in range(x-1,i,-1):
        if arr[i]>arr[j] and decrease[i]<decrease[j]:
            decrease[i] = decrease[j]
    decrease[i]=decrease[i]+1


for i in range(x):
    dp[i] = increase[i]+decrease[i] -1

print(max(dp))