import sys

nations=list(input().split())
nationsPoint={}

for i in nations:
    nationsPoint[i]=0

perTable=[]
for i in range(6):
    perTable.append((list(input().split())))

for i in perTable:
    maxValue = max(i[2:5])  # 최고확률
    maxCnt = i.count(max(i[2:5]))  # 최고확률 동률체크
    if maxValue == i[2] and maxCnt == 1:
        # 앞이 팀 이길 때
        nationsPoint[i[0]] = nationsPoint[i[0]] + 3
    elif (maxValue == i[3] and maxCnt == 1) or (maxValue != i[3] and maxCnt == 2):
        # 비길확률이 가장크거나, 이길확률==질확률일때
        nationsPoint[i[0]] = nationsPoint[i[0]] + 1
        nationsPoint[i[1]] = nationsPoint[i[1]] + 1
    else:
        # 뒤 팀이 이길 때
        nationsPoint[i[1]] = nationsPoint[i[1]] + 3

n=[]
for i in nations:
    n.append(nationsPoint[i])

s=sorted(n,reverse=True)

a=([0]*4)

for i in range(0,4):
    for j in range(0,4):
        if(s[i]==n[j]):
            a[i]=j
            if (i > 0):
                if (a[i - 1] ==a[i]):
                    a[i]=j+1
            break


if(s[0]==s[1]==s[2]==s[3]):
    for _ in range(4):
        print("%0.10f"%float(2/4))
    sys.exit()

if(s[0]==s[1]==s[2]):
    for i in range(3):
        n[a[i]]=float(2/3)
    n[a[3]]=0
    for i in range(4):print("%0.10f"%n[i])
    sys.exit()

if(s[1]==s[2]==s[3]):
    n[a[0]] = 1
    for i in range(1,4):
        n[a[i]]=float(1/3)
    for i in range(4):print("%0.10f"%n[i])
    sys.exit()

if(s[0]==s[1] or s[2]==s[3]):
    n[a[0]] = 1
    n[a[1]] = 1
    n[a[2]] = 0
    n[a[3]] = 0
    for i in range(4):print("%0.10f"%n[i])
    sys.exit()

if(s[1]==s[2]):
    n[a[0]] = 1
    n[a[1]] = float(1/2)
    n[a[2]] = float(1/2)
    n[a[3]] = 0
    for i in range(4):print("%0.10f"%n[i])
    sys.exit()
else:
    n[a[0]] = 1
    n[a[1]] = 1
    n[a[2]] = 0
    n[a[3]] = 0
    for i in range(4): print("%0.10f" % n[i])
    sys.exit()
