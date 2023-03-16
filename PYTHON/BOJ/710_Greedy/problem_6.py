# 1202번  보석 도둑
import sys
import heapq
# n : 보석 개수  k : 가방
n, k = map(int, sys.stdin.readline().split())
# m : 무게  v : 가격
jew=[]
for i in range(n):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags=[]
for i in range(k):
    bags.append(int(input()))
bags.sort()
# 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값
tmp=[]
ans=0
for bag in bags:
    # 아직 보석이 있고 가방에 담길 수 있다면 tmp에 넣음
    while jew and bag>=jew[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jew)[1])
    if tmp:
        ans+=heapq.heappop(tmp)

    if not jew:
        break
print(-ans)