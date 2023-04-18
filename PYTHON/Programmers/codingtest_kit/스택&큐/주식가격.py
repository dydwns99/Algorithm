# 가격이 떨어지지 않은 기간은 몇 초인지를 return
from collections import deque
def solution(prices):
    # 1을 스택에 넣고 그 다음은 2 그 다음은 3,,,,
    # 그 다음에 보자 작은 수가 왔다면 pop
    # 처음 떨어지기 전까지의 시간을 구하는 것임
    answer=[]
    prices = deque(prices)
    while prices:
        c= prices.popleft()
        count=0
        for i in prices:
            if c>i:
                count+=1
                break
            count+=1
        answer.append(count)
  
    return answer
print(solution([1, 0, 1, 1, 3]))