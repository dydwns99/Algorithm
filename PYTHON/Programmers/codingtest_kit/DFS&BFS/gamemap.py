# bfs, graph , deque
from collections import deque
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[0]):
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph
def solution(maps):
    global graph
    graph=maps

    new_graph=bfs(0,0)
    print("new_graph", new_graph)
    if new_graph[len(new_graph)-1][len(new_graph[0])-1]==1:
        answer=-1
    else:
        answer=new_graph[len(new_graph)-1][len(new_graph[0])-1]

    return answer



solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
