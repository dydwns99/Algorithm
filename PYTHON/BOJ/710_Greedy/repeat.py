# 1285번  동전 뒤집기
# n x n 
import sys
n = int(input())
# 동전
coin=[0] * n
for i in range(n):
    # 한줄을 입력 받고 
    for j,c in zip(range(n-1,-1,-1), sys.stdin.readline().strip()):
        if c=='T':
            coin[i]+= (1<<j)
            # 000
            #  00
            #   1
            # 위치로만 봐야함
count=0
sum=0
ans=n*n
# 열에 있는 동전을 다 바꾸는 경우의 수
for flip in range(1<<n):
    # coin 의 행 마다
    for c in coin:
    # 행 ^ flip 을 하고  1의 개수를 셈
        count = bin(c ^ flip).count("1")
    # 그 후 적은 개수를 더함
        sum+= min(count, n-count)
    ans=min(ans,sum)
print(ans)
