m1=([0]*7)
m1[0]=int(0)
m1[1]=int(5000000)
m1[2]=int(3000000)
m1[3]=int(2000000)
m1[4]=int(500000)
m1[5]=int(300000)
m1[6]=int(100000)

m2=([0]*6)
m2[0]=int(0)
m2[1]=int(5120000)
m2[2]=int(2560000)
m2[3]=int(1280000)
m2[4]=int(640000)
m2[5]=int(320000)


def Num1(n):
    if(n==1):return int(1)
    elif(n==0):return int(0)
    elif(2 <= n <= 3):return int(2)
    elif (4 <= n <= 6):return int(3)
    elif (7 <= n <= 10):return int(4)
    elif (11 <= n <= 15):return int(5)
    elif (16 <= n <= 21):return int(6)
    else:return int(0)

def Num2(n):
    if(n==1):return int(1)
    elif (n == 0):return int(0)
    elif(2 <= n <= 3):return int(2)
    elif (4 <= n <= 7):return int(3)
    elif (8 <= n <= 15):return int(4)
    elif (16 <= n <= 31):return int(5)
    else:return int(0)

t=int(input())
for _  in range(t):
    x,y=map(int,input().split())
    print(m1[Num1(x)]+m2[Num2(y)])