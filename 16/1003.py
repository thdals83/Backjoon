c0=[1,0,1]
c1=[0,1,1]

def dp(x):
    l=len(c0)
    if l<=x:
        for i in range(l,x+1):
            c0.append(c0[i-1]+c0[i-2])
            c1.append(c1[i-1]+c1[i-2])
    print('%d %d'%(c0[x],c1[x]))

if __name__=="__main__":
    x=int(input())
    num=[]
    for _ in range(x):
        y=int(input())
        dp(y)


'''
t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)
'''