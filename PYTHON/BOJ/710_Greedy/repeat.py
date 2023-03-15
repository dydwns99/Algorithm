# 11047번 동전 0
# n : 동전의 종류 개수 , k : 가치의 합
n, k = map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
# k를 만들기 위해 필요한 동전 개수의 최솟값
# 가격이 제일 큰 동전부터 다 써보고 초과된다면 그 다음 동전으로 써봄
count=0
for i in range(n-1,-1,-1):
    # 4200//1000
    count+=k//coins[i]
    if k%coins[i] == 0:      
        break
    k=k%coins[i]
print(count)