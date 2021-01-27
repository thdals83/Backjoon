x= int(input())

arr=[]

for i in range(x):
    (a,b)=map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x:(x[1],x[0]))

res=1
end=arr[0][1]

for i in range(1,x):
    if end<=arr[i][0]:
        res+=1
        end = arr[i][1]


print(res)