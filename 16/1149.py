n=int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1, len(arr)):
    arr[i][0] = arr[i][0] + min(arr[i - 1][1], arr[i - 1][2])
    print(arr[i][0])
    arr[i][1] = arr[i][1] + min(arr[i - 1][0], arr[i - 1][2])
    print(arr[i][1])
    arr[i][2] = arr[i][2] + min(arr[i - 1][0], arr[i - 1][1])
    print(arr[i][2])
print(min(arr[n-1][0],arr[n-1][1],arr[n-1][2]))