# 1285번  동전 뒤집기
# n 행 n 열
n = int(input())
# H : 앞면  T : 뒷면
coins=[]
coins=[0]*n
# 한행, 한열에 있는 동전들을 모두 뒤집는 작업들을 수행해 
# 뒷면이 위를 향해 놓일 수 있는 동전의 최소 개수

# 앞면 : 0  뒷면 : 1
for i in range(n):# 2 1 0   /   H H T
    for j, c in zip(range(n-1,-1,-1), input().strip()):
        if c=='T':
            coins[i]+=(1<<j)  # 000 + 00 + 1
    
# 첫 행부터  열들을 뒤집음
answer=n*n
for i in range(1<<n): # 열들을 뒤집는 모든 경우의 수
    tmp=0
    for j in range(n):
        # i(000) 와 행들을 xor 함
        count=bin(coins[j]^i).count('1')
        tmp +=min(count, n-count)# 행에 있는 동전 중 1 인 동전만 count 함
    answer=min(answer,tmp)
print(answer)


