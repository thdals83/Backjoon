#유클리드 호제법 이용
#두 수 a와 b (a>b)가 있다고 할 때, 최대공약수 G는 a%b(a를 b로 나눈 나머지) 이다.

x,y = map(int, input().split())
x1=x
y1=y
while y!=0:
    x=x%y
    x,y=y,x



print(x)
print(x1*y1//x)