x= int(input())

arr=list(map(int,input().split()))
arr.sort()
full=arr[0]
res=arr[0]
for i in range(1,x):
    full=arr[i]+full
    res=res+full



print(res)