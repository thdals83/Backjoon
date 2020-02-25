n=int(input())
a={}

for i in range(n):
    x,y=map(int,input().split())
    a[y]=a.get(y,[])+[x]

arr=sorted(a.items())

for i in range(len(arr)):
    arr2=sorted(a[arr[i][0]])
    for j in arr2:
        print(j,arr[i][0])