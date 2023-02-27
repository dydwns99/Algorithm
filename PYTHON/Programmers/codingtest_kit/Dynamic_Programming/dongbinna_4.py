# 금광 조지기

# d[n][m] = max(d[n][m-1], d[n-1][m-1], d[n+1][m-1])+a[n][m]

n, m = map(int, input().split())
array = list(map(int,input().split()))
mount=[]
for i in range(n):
    sub=[]
    for j in range(m):
        sub.append(array.pop(0))
    mount.append(sub)

dp=[[0]*m for _ in range(n)]
for i in range(n):
    dp[i][0]=mount[i][0]
print("금광 채굴 과정 ...")
for i in range(1,m):
    for j in range(n):
        if j==0: left_down=0
        else : left_down =dp[j-1][i-1]
        if j==n-1: left_up = 0
        else : left_up =dp[j+1][i-1]
        left = dp[j][i-1]
        dp[j][i]=max(left_down,left_up,left)+mount[j][i]

    for i in range(n):
        print(dp[i])
    print("----")
# for i in range(n):
#     print(dp[i])
