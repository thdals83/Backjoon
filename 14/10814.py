x=int(input())

arr={}


for _ in range(x):
    x,y=input().split()
    x=int(x)
    arr[x]=arr.get(x,[])+[y]


arr2=sorted(arr.items())
arr2=dict(arr2)


for i in arr2.keys():
    for j in range(len(arr2[i])):
        print(i,arr2[i][j])

