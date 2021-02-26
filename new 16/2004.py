def num(k, n):
    count = 0
    while(k != 0):
        k = k // n
        count += k
    return count

n, m = list(map(int, input().split()))

five = num(n, 5) - num(m, 5) - num(n-m, 5)
two = num(n, 2) - num(m, 2) - num(n-m, 2)

print(min(five, two))