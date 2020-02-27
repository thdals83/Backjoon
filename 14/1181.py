x=int(input())
arr=[]

for _ in range(x):
    n=str(input())
    arr.append(n)

arr=set(arr)
arr=list(arr)

arr.sort()
arr.sort(key=lambda x:len(x))

for i in arr:
    print(i)

"""
for i in arr:
    use[len(i)]=use.get(len(i),[])+[i]
    num.append(len(i))

num=set(num)
num=list(num)

for i in num:
    arr2=sorted(use[i])
    for j in arr2:
        print(j)
"""


