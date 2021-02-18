def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


x = int(input())

for _ in range(x):
    n, m = map(int, input().split())
    res = factorial(m) // (factorial(n) * factorial(m - n))
    print(res)

"""
import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    res = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(res)
"""