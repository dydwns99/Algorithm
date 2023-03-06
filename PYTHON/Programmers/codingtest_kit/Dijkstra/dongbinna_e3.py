# 다익스트라 알고리즘 :  개선된
import heapq

INF = int(1e9) # 무한 의미
# n : 노드의 개수 , m : 간선의 개수 
n, m = map(int, input().split())
# start : 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
graph=[[] for i in range(n+1)] # node 1 ~ node n
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
# graph[해당 노드].[연결노드, 거리]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    hq=[]
    distance[start]=0
    heapq.heappush(hq, (0, start))
    while hq:
        #dist : now 노드가 보유한 거리
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
            heapq.heappush(hq, ( cost, i[0]))
