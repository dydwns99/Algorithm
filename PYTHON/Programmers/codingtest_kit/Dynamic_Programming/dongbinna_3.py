# M 원을 만들기 위한 최소한의 화폐 개수
n, m = map(int,input().split())
moneys=[]
for _ in range(n):
    moneys.append(int(input()))
dp=[10000]*(m+1)


for i in range(min(moneys),m+1): # 3,4
    for money in moneys: # 3,5,7
        if i-money==0:
            dp[money]=1
    # 크다면 뺀 수랑 비교해봄
        if i-money>0 :
            dp[i]=min(dp[i-money]+1, dp[i])

if dp[m]==10000:
    print("-1")
else:
    print(dp[m])
            

