x=int(input())

check=0
for i in range(x):
    res=use=i

    while use>0:
        res=res+(use%10)
        use=use//10

    if(res==x):
        check=1
        print(i)
        break

if(check==0):
    print(0)