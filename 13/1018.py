N,M=map(int,input().split())

arr=[]
res=None
for i in range(N):
    row=input()
    row_list=list(row)
    arr.append([])
    for j in row_list:
        arr[i].append(j)

for i in range(N-8+1):
 for j in range(M-8+1):
     num1=0
     num2=0
     for k in range(i,i+8):
         for l in range(j,j+8):
             if((k+l-i-j)%2==0):
                 if(arr[k][l]=='B'):num1=num1+1
             else:
                 if(arr[k][l]=='W'):num1=num1+1

     for k in range(i,i+8):
         for l in range(j,j+8):
             if((k+l-i-j)%2==0):
                 if(arr[k][l]=='W'):num2=num2+1
             else:
                 if(arr[k][l]=='B'):num2=num2+1

     if(res == None):res=min(num1,num2)
     else:
         if(res>min(num1,num2)):res=min(num1,num2)

print(res)