# 다익스트라
import heapq

# 필요한 것
# 노드 개수, 간선 개수, 
v, e = map(int, input().split())
# 그래프 정보 표시
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
# 거리 정보
INF=int(1e9)
distance=[INF]*(v+1)
# 시작 노드
start = int(input())

def dijkstra(start):
    hq=[]
    distance[start]=0
    heapq.heappush(hq, (0,start))
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for g in graph[now]:
            cost = g[0]+dist
            if distance[g[1]]>cost:
                distance[g[1]]=cost
            heapq.heappush(hq, (cost,g[1]))





    





