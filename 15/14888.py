from itertools import permutations

if __name__=="__main__":
    n=int(input())
    num = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    oper=[]
    for i in range(4):
        for j in range(arr[i]):
            oper.append(i)

    oper=set(permutations(oper,n-1))
    oper=list(oper)

    check=False
    for i in range(len(oper)):
        x=1
        tmp=num[0]
        for j in range(len(oper[i])):
            if (oper[i][j] == 0):
                tmp=tmp + num[x]
                x = x + 1
            elif (oper[i][j] == 1):
                tmp = tmp - num[x]
                x = x + 1
            elif (oper[i][j] == 2):
                tmp = tmp * num[x]
                x = x + 1
            else:
                if(tmp<0):
                    tmp = -tmp
                    tmp = tmp//num[x]
                    tmp = -tmp
                    x = x + 1
                else:
                    tmp = tmp // num[x]
                    x = x + 1
        if(check==False):
            max=tmp
            min=tmp
            check=True
        else:
            if(max<tmp):max=tmp
            if(min>tmp):min=tmp

print(max)
print(min)

'''

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)
'''

