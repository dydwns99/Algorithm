# 꼭대기에서 바닥까지 거쳐간 숫자의 합이 가장 큰  경우, 대각선으로만 이동
# an
def solution(triangle):
    # dp => 그 원소에 이르기 까지의 최댓값
    # dp[n][m] = max(dp[n-1][m-1], dp[n-1][m])+arr[n][m]
    # if m==왼쪽끝 : dp[n][m]=dp[n-1][m]+arr[n][m]
    # if m==오른쪽끝 : dp[n][m]=dp[n-1][m-1]
    dp=[]
    
    for i in range(len(triangle)):
        sub=[]
        for j in range(0,i+1):
            sub.append(0)
        dp.append(sub)
    dp[0]=triangle[0]

    for n in range(1,len(dp)): # 1<= n <5
        for m in range(n+1): # 0<= n <2
            if m==0: left=dp[n-1][m]
            else: left=dp[n-1][m-1]
            if m==n: right=dp[n-1][m-1]
            else: right=dp[n-1][m]
            dp[n][m]=max(left,right)+triangle[n][m]
    answer=max(dp[len(dp)-1])
    return answer
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
