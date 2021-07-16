n,k = map(int,input().split())

arr=[]
x=0

for i in range(n):
    arr.append((int(input())))

for i in range(n-1,-1,-1):
    if k==0:
        break
    if arr[i]>k:
        continue
    x += k//arr[i]
    k%=arr[i]

print(x)    