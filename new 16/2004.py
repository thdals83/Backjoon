def main():
    arr=list(input().split())
    n=int(input())
    arr2=[]
    for _ in range(n):
        arr2.append(list(input().split()))

    for i in arr2:
        print(i)


if __name__ == "__main__":
    main()