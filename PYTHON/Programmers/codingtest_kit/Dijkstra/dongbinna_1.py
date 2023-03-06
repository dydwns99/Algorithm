# 도시 개수 : N, 통로 개수 : M, 메시지 보내고자 하는 도시 : C
INF=1e9
n, m, c = map(int, input().split())

road =[ [] for i in range(n+1)]
for _ in range(m):
    info = list(map(int,input().split()))
    road[info[0]].append((info[1],info[2]))
distance=[INF] * (n+1)

import heapq
def dijkstra(start):
    hq=[]
    distance[start]=0
    heapq.heappush(hq,(0,start))
    while hq:
        # dist : now노드 안에 있는 수
        dist, now = heapq.heappop(hq)
        #이미 참조가 되어있으면 continue
        if distance[now] <dist:
            continue
        for i in road[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]]=cost
            heapq.heappush(hq,(cost,i[0]))
dijkstra(c)
count =0
max_distance=0
for d in distance:
    if d!=1e9:
        count+=1
        max_distance = max(max_distance,d)
print(count-1,max_distance)