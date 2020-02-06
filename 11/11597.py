def hanoi(n,frm,tmp,to):
    if (n==1):print(frm,to)
    else:
        hanoi(n-1,frm,to,tmp)
        print(frm,to)
        hanoi(n-1,tmp,frm,to)




if __name__=="__main__":
    x=int(input())
    print((2**x)-1)
    hanoi(x,1,2,3)