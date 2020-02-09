import math

def Dispersal(m,array):
    sum=0
    for i in array:
        sum=sum+((i-m)**2)

    sum=sum/len(array)
    return sum

x,y=map(int,input().split())
arr=list(map(int,input().split()))

first=0
end=y-1
add=list()

while end<=x-1:
    tmp=arr[first:end+1]
    m=sum(tmp)/len(tmp)
    add.append(Dispersal(m,tmp))
    first=first+1
    end=end+1

res=min(add)
print(float(math.sqrt(res)))
