x=int(input())
dis=list(map(int,input().split()))
pri=list(map(int,input().split()))
start=0
check=0
res=0
for i in range(x):
    if pri[check]>pri[i]:
        res=res+pri[check]*sum(dis[check:i])
        check=i
if check!=x-1:
    res = res + pri[check] * sum(dis[check:i])

if res==0:
    res = pri[check] * sum(dis)

print(res)