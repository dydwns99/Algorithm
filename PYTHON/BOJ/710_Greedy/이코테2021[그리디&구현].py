#현재 상황에서 지금 당장 좋은 것만 고르는 방법 -> 최적의 해를 보장 할 수 없을 때가 많음. -> 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론 할 수 있어야 풀리도록 문제 출제


#거스름돈 문제
#가장 큰 화페 단위 부터 돈을 거슬러줌
# 큰 단위가 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
# 시간 복잡도 -> O(k)

# 1이 될 때까지
# n 의 제곱근의 정수 를 추출  27, 5 25 125
# n // k + n % k

n,k =map(int, input().split())
# 가능한 나누기 먼저 하고, 아니면 뺌

result=0
while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    if n<k :
        break
    result +=1
    n //= k
result += (n-1)
print(result)


# 곱하기 혹은 더하기 해서 만들어 질 수 있는 가장 큰 수
# 가능한 곱하기를 가장 많이, 근데 0 이 있으면 더해줌
strs = input()
nums=[]
for i in strs:
    nums.append(int(i))
# result = 1
print(nums)
result = nums[0]
for n in range(1,len(nums)):
    if nums[n] == 0 or nums[n] == 1:
        result += nums[n]        
    else:
        result *= nums[n] 
print(result)


# 모험가 길드 문제
# 여행 떠날 수 있는 그룹 수의 최댓값
# 그냥 공포도 제일 낮은 친구 부터  맞춰서 보내면 되지 않나?

n = int(input())

# data = list(map(int, input().split()))
exp = input().replace(" ","")
num = []
for i in exp:
    num.append(int(i))

num.sort()  

group=[]
count=0
for i in range(0,len(num)):
    group.append(num[i])
    if num[i] <= len(group):
        count += 1
        group.clear()
print(count)

# for i in range(n):
#     num = int(exp[i]) 

# 1931번  회의실 배정
