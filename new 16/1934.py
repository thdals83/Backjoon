#유클리드 호제법을 이용한 최소공배수 구하기
#두 수 a,b(a>b)가 있을 때 최대 공약수는 G(a,b)는 a를 b로 나눈 나머지 이다.
n=int(input())

for _ in range(n):
    x,y=map(int,input().split())
    x1=x
    y1=y
    while y!=0:
        x=x%y
        x,y=y,x


    print(x1*y1//x)