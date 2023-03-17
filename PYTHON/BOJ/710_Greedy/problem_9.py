# 12015번  가장 긴 증가하는 부분 수열 2
# 수열 A 의 크기
n = int(input())
# 수열 A
cases=list(map(int, input().split()))

# 인덱스 x 까지 만들 수 있는 수열의 길이를 표시함 -> 시간 초과 O(n^2)
# 이분탐색으로 해결! -> O(nlog n)

lis = [0]

for case in cases:
    # 마지막 원소보다 크다면 일단 집어 넣음
    if lis[-1]<case:
        lis.append(case)
    # 작다면 구성된 배열에서 
    # 이분 탐색을 통해 case와 원래 있던 원소를 교체 
    # -> LIS 의 길이는 같게 구할 수 있지만
    # 배열에 들어있는 값들은 LIS가 이루는 요소와는 전혀 무관하다
    else:
        left = 0
        right = len(lis)

        while left<right:
            mid = (right+left)//2
            if lis[mid]<case:
                left = mid+1
            else:
                right = mid
        lis[right] = case
print(len(lis)-1)