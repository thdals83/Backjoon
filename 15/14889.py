import sys
import math
from itertools import combinations

n=int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int, input().split())))

people=list(range(n))
candidate=list(combinations(people,n//2))

res=math.inf

for group in candidate:
    rest=list(set(people)-set(group))

    sum1=0
    sum2=0
    use=list(combinations(list(group), 2))
    use2=list(combinations(rest, 2))

    for y,x in use:
        sum1= sum1 + (arr[y][x] + arr[x][y])
    for y, x in use2:
        sum2 = sum2 + (arr[y][x] + arr[x][y])

    if res>abs(sum1 - sum2): res=abs(sum1 - sum2)

print(res)