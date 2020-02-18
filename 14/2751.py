def mergeSort(input_list):
    if len(input_list) > 1:

        mid = int(len(input_list) / 2)

        Leftlist = input_list[:mid]
        Rightlist = input_list[mid:]

        mergeSort(Leftlist)
        mergeSort(Rightlist)

        Lidx, Ridx, idx = 0, 0, 0

        while Lidx < len(Leftlist) and Ridx < len(Rightlist):
            if Leftlist[Lidx] < Rightlist[Ridx]:
                input_list[idx] = Leftlist[Lidx]
                Lidx += 1
            else:
                input_list[idx] = Rightlist[Ridx]
                Ridx += 1

            idx += 1

        while Lidx < len(Leftlist):
            input_list[idx] = Leftlist[Lidx]
            Lidx += 1
            idx += 1

        while Ridx < len(Rightlist):
            input_list[idx] = Rightlist[Ridx]
            Ridx += 1
            idx += 1


if __name__ == "__main__":
    n = int(input())
    arr = []

    for _ in range(n):
        x = int(input())
        arr.append(x)

    mergeSort(arr)

    for i in arr:
        print(i)