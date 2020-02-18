import sys

n=int(sys.stdin.readline())

list=[]
res_list=[0]*10001


for i in range(n):
    x=int(sys.stdin.readline())
    res_list[x]=res_list[x]+1

for i in range(len(res_list)):
    for j in range(res_list[i]):
        print(i)