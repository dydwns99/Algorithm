# 모든 사람이 심사 받는데 걸리는 시간을 최소로

# n : 입국 심사 기다리는 사람 수   
# times[] : 각 심사관들의 심사 시간

# n=6  times=[7,10]
def solution(n, times):
 
    # 최소 시간 n/len(times)*min(times) = 21
    # 최대 시간 6*10 = 60
    # 그거의 mid 찾고 , mid 값으로 채울 수 있나 확인
    start = 1
    end = n*max(times)
    while start<=end:
        mid= (start+end)/2
        people =0
        for time in times:
            people += mid // time
            if people>=n:
                break
        if people>=n:
            answer = mid
            end = mid -1
        elif people<n:
            start = mid + 1
    return answer

