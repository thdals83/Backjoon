def gcd(x,y):
    mod=x%y
    while mod>0:
        x=y
        y=mod
        mod = x%y
    return y

def div(x):
    dlist=[x]
    for i in range(2, int(x**(1/2) +1)):
        if x%i ==0:
            dlist.append(i)
            if x//i !=i:
                dlist.append(x//i)
    dlist.sort()
    return dlist

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

res=[]
for i in range(len(arr)-1):
    res.append(arr[i]-arr[i+1])

if len(res)==1:
    res2=res[0]
elif len(res)==2:
    res2=gcd(res[0],res[1])
else:
    res2=res[0]
    for i in range(1,len(res)):
        res2=gcd(res2,res[i])

for i in div(res2):
    print(i, end = ' ')
