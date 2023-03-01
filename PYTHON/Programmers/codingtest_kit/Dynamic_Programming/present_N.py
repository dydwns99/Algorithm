# N 여러개로 사칙연산을 수행하여 number 만들고 사용한 N의 개수의 최솟값 출력
def solution(N,number):
    # 5 로 12 만드는방법
    # + - x / 붙임
    # dp[1]=2 dp[11]=3 dp[111]=4 ...
    # dp[2]=3 dp[3]=4 dp[4]=5
    # dp[5]=1 dp[10]=2 dp[15]=3... dp[25]=5
    # dp[25]=2 dp[125]=3
    dp=[10000]*32001
    # 먼저 N이 갖는 특징의 수들은 먼저 넣어주고
    for i in range(len(dp)//5):
        dp[N*i]=i
    for i in range(5):
        dp[11**i]=i+2
    for i in range(7):
        dp[N**i]=i
    print(dp)
    
    for i in range(2,32001):
        dp[i]=min(dp[i-1]+1)
    #12
    # dp[n]= min(dp[n-1]+2, )
    #   if n/5 ==0 : dp[n],     
    #   else n/5 != 0 : dp[n/5] + dp[n%5]
    #   13 -> dp[55/5]+(5+5)/5
    #   14 -> dp[55/5]] + dp[4] , 5+5+(5+5+5+5)/5


    ############## => 1개, 2개, ... 8개 까지 경우를 모두 구하면서 number 찾음
    
    answer=0
    return answer
solution(5,12)
