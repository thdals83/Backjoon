import sys

tmp=[0]*1000001

def dp(x):
    tmp[1]=1
    tmp[2]=2

    for i in range(3,x+1):
        tmp[i]=(tmp[i-1]+tmp[i-2])%15746
    return tmp[x]

if __name__=="__main__":
    x=int(sys.stdin.readline())
    print(dp(x))



'''
배열 안쓰는 방법

import sys
n = int(sys.stdin.readline())
f = 1
s = 2
tmp = 0
for i in range(n - 1):
    tmp = f
    f = s
    s = (tmp + s) % 15746
print(f)
'''