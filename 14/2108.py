import sys
from collections import Counter

def avg(arr):
    return round(sum(arr)/len(arr))

def middle(arr):
    return arr[len(arr)//2]

def many(arr):
    dic=Counter(arr)
    res=dic.most_common()

    if(len(arr)>1):
        if(res[0][1]==res[1][1]):return res[1][0]
        else:return res[0][0]

    else:return res[0][0]

def ran(arr):
    return max(arr)-min(arr)

if __name__=="__main__":
    n=int(sys.stdin.readline())
    arr=[]

    for _ in range(n):
        x=int(sys.stdin.readline())
        arr.append(x)
    arr.sort()

    print(avg(arr))
    print(middle(arr))
    print(many(arr))
    print(ran(arr))