if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    move = []
    cloud = [[n-2, 0], [n-2, 1], [n - 1, 0], [n - 1, 1]]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for _ in range(n):
        arr.append(list(map(int, input().split())))
    for _ in range(m):
        x,y = map(int, input().split())
        move.append([x-1,y])

#########################################
    print(n, m)
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    for i in move:
        for j in i:
            print(j, end=" ")
        print()
#########################################

    for i in range(m):
        #구름 이동
        mov = move[i]
        next_cloud = []
        for tmp in cloud:
            x = tmp[0]
            y = tmp[1]
            d = mov[0]
            s = mov[1]
            next_x = (n + x + dx[d] * s) % n
            next_y = (n + y + dy[d] * s) % n
            next_cloud.append([next_x,next_y])

        #물 양 증가시키기


    res = 0
    for i in range(len(arr)):
        res += sum(arr[i])
    print(res)




