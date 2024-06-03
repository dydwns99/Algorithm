# 동전 0

# n -> 동전 종류 / k -> 만들 값
# 동전 개수 최소로 해서 k 값 만들기
# 

n, k = map(int,input().split())
coins = []

for i in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)
# for a in range(n):
#     print(coins[a])


count = 0
# 나머지가 0이 될 때 까지 큰 수 부터 k를 나눠줌
for i in range(n):
    if k == 0:
        break
    if coins[i] <= k:
        #print(k," / ", coins[i])
        count += int(k/coins[i])
        k = k%coins[i]
        #print("사용한 동전 개수 ",count)
print(count)
    
