"""
from collections import Counter
x = int(input())
for i in range(x):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        s.append(b)
    num = 1
    result = Counter(s)
    for key in result:
        num *= result[key] + 1
    print(num - 1)
"""


x = int(input())

for _ in range(x):
    n = int(input())

    # 0일때 탈출
    if n == 0:
        print(0)
        continue

    arr = dict()
    for _ in range(n):
        name, type = map(str, input().split())

        # 같은 옷 분류 중, 이름은 버리고 종류만 가져가기
        if type in arr.keys():
            arr[type] += 1
        else:
            arr[type] = 1

        # (각 옷의 수)+1 한 것을 곱해줌
        res = 1
        for key in arr.keys():
            res *= arr[key] + 1
    # 안입는 경우만 뺴줌
    print(res - 1)