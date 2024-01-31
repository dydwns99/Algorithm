#현재 상황에서 지금 당장 좋은 것만 고르는 방법 -> 최적의 해를 보장 할 수 없을 때가 많음. -> 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론 할 수 있어야 풀리도록 문제 출제


#거스름돈 문제
#가장 큰 화페 단위 부터 돈을 거슬러줌
# 큰 단위가 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
# 시간 복잡도 -> O(k)

# 1이 될 때까지
# n 의 제곱근의 정수 를 추출  27, 5 25 125
# n // k + n % k

# n,k =map(int, input().split())
# 가능한 나누기 먼저 하고, 아니면 뺌

# result=0
# while True:
#     target = (n//k) * k
#     result += (n-target)
#     n = target
#     if n<k :
#         break
#     result +=1
#     n //= k
# result += (n-1)
# print(result)


# 곱하기 혹은 더하기 해서 만들어 질 수 있는 가장 큰 수
# 가능한 곱하기를 가장 많이, 근데 0 이 있으면 더해줌
# strs = input()
# nums=[]
# for i in strs:
#     nums.append(int(i))
# # result = 1
# print(nums)
# result = nums[0]
# for n in range(1,len(nums)):
#     if nums[n] == 0 or nums[n] == 1:
#         result += nums[n]        
#     else:
#         result *= nums[n] 
# print(result)


# 모험가 길드 문제
# 여행 떠날 수 있는 그룹 수의 최댓값
# 그냥 공포도 제일 낮은 친구 부터  맞춰서 보내면 되지 않나?

# n = int(input())

# data = list(map(int, input().split()))
# exp = input().replace(" ","")
# num = []
# for i in exp:
#     num.append(int(i))

# num.sort()  

# group=[]
# count=0
# for i in range(0,len(num)):
#     group.append(num[i])
#     if num[i] <= len(group):
#         count += 1
#         group.clear()
# print(count)

######################################################
# 구현 문제 : 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

# 1. 행렬
# for i in range(5):
#     for j in range(5):
#         print('(', i, ',', j, ')', end=' ')
#     print()

# dx = [0,-1,0,1]
# dy = [1,0,-1,0]
# x, y = 2,2
# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

# 상하좌우 문제
# n = int(input())
# move=input().split(" ")
# print(move)
# x, y = 1,1
# m_type = ['L', 'R', 'U', "D"]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# for i in range(5):
#     for j in range(len(m_type)):
#         if move[i]==m_type[j]:
#             nx = x + dx[j]
#             ny = y + dy[j]

#     if nx < 1 or ny < 1 or nx >n or ny > n:
#         continue
#     x,y = nx, ny
# print('(',x,',', y,')')

# 시각 문제
# n = int(input()) # 0시 0 0 ~ n시 59 59

# # 0~23 0~59 0~59

# count=0
# for i in range(n+1):
#     for j in range(60):
#         for x in range(60):
#             if '3' in str(i) + str(j) + str(x):
#                 count+=1
# print(count)

# 왕실의 나이트
# 8x8
loc = input()
# a를 숫자로...

x,y = ord(loc[0]) - ord('a') + 1, int(loc[1])
dx = [-1,1,-1,1,-2,2,-2,2]
dy = [-2,-2,2,2,-1,-1,1,1]
count=0
# dx 먼저 or dy 먼저
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue

    count+=1
print(count)


