# 11399번  ATM
# n : 사람 수
n = int(input())
# 각 사람이 인술하는데 걸리는 시간
p = list(map(int, input().split()))

# 각 사람의 돈을 인출 하는데 필요한 시간의 합의 최솟값

# 인출 시간을 오름 차순
p.sort()
# 더한 값을 배열에 저장
ans=0
sum=0
for i in range(n):
    sum+=p[i]
    ans+=sum
print(ans)
# 그 배열의 총합 구함