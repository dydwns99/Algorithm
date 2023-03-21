# 위상 정렬
from collections import deque

# v : 노드 개수 , e : 간선 개수
v, e = map(int,input().split())
# 노드의 진입 차수는 0 으로 초기화
indegree=[0]*(v+1) 
# 노드에 대한 간선 정보
graph =[[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

# 위상 정렬 함수
def topology_sort():
    result=[]
    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    # 큐가 빌때까지
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i, end=" ")

topology_sort()