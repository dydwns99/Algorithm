# 섬 연결하기
import heapq

num=0
INF=int(1e9)
graph=[]
distance=[]

 # 다익스트라 알고리즘
def dijkstra(start):
    hq=[]
    global distance
    distance=[INF]*num
    distance[start]=0
    line=[0]*num
    heapq.heappush(hq,(0, start))

    while hq:
        dist, node = heapq.heappop(hq)

        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                line[i[0]]=i[1]
                heapq.heappush(hq, (cost,i[0]))
    # print(line)
    return line
    # print("사용한 길 : ",line)
def solution(n,costs):
    
    # 최소비용으로 모든 섬이 서로 통행 가능하도록 최소비용 리턴
    global num
    num = n
    global graph
    graph = [[]*3 for i in range(num)]
    
    for cost in costs:
        graph[cost[0]].append((cost[1],cost[2]))
        graph[cost[1]].append((cost[0],cost[2]))
    # print("graph : ", graph)
    answer = INF
    for i in range(n):
        answer = min(answer, sum(dijkstra(i)))

    return answer
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

