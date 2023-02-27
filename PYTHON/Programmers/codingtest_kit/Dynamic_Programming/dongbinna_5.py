# 병사 배치하기
# 전투력 내림차순되게 배치 단, 열외시켜 최대한 길게 만들 수 있으면 그렇게 함
n = int(input())

soliders = list(map(int,input().split()))
soliders.reverse()

dp=[1]*n
# 가장 긴 증가하는 부분 수열 LIS
# 각 병사까지 최대 길이를 구함
for i in range(1,n):
    for j in range(0,i):
        if soliders[j]<soliders[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
        
