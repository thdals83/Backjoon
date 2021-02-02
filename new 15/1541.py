x= input().split('-')

res=[]
for i in x:
    num=0
    tmp=i.split('+')
    for j in tmp:
        num=num+int(j)

    res.append(num)

fin=res[0]

for i in range(1,len(res)):
    fin=fin-res[i]

print(fin)