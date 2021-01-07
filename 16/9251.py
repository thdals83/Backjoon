x=list(input())
y=list(input())

xnum=len(x)
ynum=len(y)

dp=[[0]*(ynum+1) for i in range(xnum+1)]

for i in range(xnum):
    for j in range(ynum):
        if x[i] == y[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i + 1][j + 1] = max(dp[i][j+1],dp[i+1][j])

print(dp[xnum][ynum])