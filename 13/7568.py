x=int(input())

arr=[]

for i in range(x):
    x,y=map(int,input().split())
    arr.append([])
    arr[i].append(x)
    arr[i].append(y)

for i in arr:
    count=0
    for j in arr:
        if(i[0]<j[0] and i[1]<j[1]):
            count=count+1
    print(count + 1, end=" ")
