summary=[]
use=[]
check=['WHO','WHAT','WHERE']
res=[]
confirm=True
while True:
    x=input()
    if(x=='0'):
        for _ in range(3):use.append(input())
        break

    if(x[len(x)-1]=='.'):
        x = x[0:len(x) - 1]
        confirm=False

    x=x.split(' ')

    if(confirm==False):
        x.append('.')

    for i in x:
        for j in check:
            if(i==j):
                res.append(j)
                check.remove(j)
    summary.append(x)

for i in range(len(summary)):
    for j in range(len(summary[i])):
        for k in range(3):
            if(summary[i][j]==res[k]):
                summary[i][j]=use[k]
                break

if(confirm==False):
    for i in range(len(summary)):
        summary[i].pop()
        summary[i][len(summary[i])-1]=summary[i][len(summary[i])-1]+'.'

for i in summary:
    print(' '.join(i))
