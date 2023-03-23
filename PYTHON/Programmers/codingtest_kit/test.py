# 다익스트라
import heapq

v, e = map(int,input().split())

graph=[[] for _ in range(e)]
for i in range(e):
    a,b,cost = map(int, input().split())
    graph[a].append((cost,b))

INF=int(1e9)
distance=[INF]*(v+1)

def dijkstra(start):
    hq=[]
    distance[start]=0
    heapq.heappush(hq,(0,start))
    while hq:
        # dist - 
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for g in graph[now]:
            cost = dist+g[0]
            if distance[g[1]]>cost:
                distance[g[1]]=cost
            heapq.heappush(hq,(cost, g[1]))

