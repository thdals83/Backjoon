# 얼음이 있는 칸 3


if __name__ == "__main__":
    N,Q = map(int,input().split())
    arr = []
    firestoms = []

    #값 입력
    for _ in range(2**N):
        arr.append(list(map(int,input().split())))
    firestoms = list(map(int,input().split()))


    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    print(firestoms)

    # 파이어 스톰 Q번 반복
    for _ in range(Q):
        # 파이어 스톰 배열 반복
        for firestom in firestoms:

            for i in range(0,N,(2**firestom)):
                for j in range(0, N, (2 ** firestom)):
                    for x in range(2 ** firestom):
                        for y in range(2 ** firestom):
                            print(arr[i + y][j + (2 ** firestom) - x - 1],end=" ")
                        print("")






