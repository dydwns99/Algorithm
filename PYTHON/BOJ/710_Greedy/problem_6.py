import sys
import heapq

n, k = map(int,sys.stdin.readline().split())
jew=[]
for _ in range(n):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags=[]
for _ in range(k):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer=0

tmp_jew=[]
# 가방을 확인
for bag in bags:
    # 보석이 아직 있고 가방이 작은거 부터 그 보석을 담을 수 있으면
    while jew and bag>=jew[0][0]:
        # 일시 보석 보관함에 음수 붙여서 가격을 넣음 -> 가격 가장 큰 것이 가장 앞으로 감
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -=heapq.heappop(tmp_jew)
    elif not jew:
        break