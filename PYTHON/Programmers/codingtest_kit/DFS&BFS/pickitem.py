# 캐릭터가 아이템을 줍기까지 경로의 최솟값
# bfs, deque
from collections import deque
graph=[[0]*20 for _ in range(20)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ix=0
iy=0
def bfs(x,y):
    global graph
    queue=deque()
    queue.append((x,y))
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx==iy and ny==ix:
                queue.append((nx,ny))
                #최소값으로 설정
                graph[nx][ny]=min(graph[nx][ny],graph[x][y]+1)
                
            if nx<0 or nx>=len(graph)-1 or ny<0 or ny>len(graph)-1 or graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny]= graph[x][y]+1
           
    return graph

def solution(rectangle, characterX, characterY, itemX, itemY):
    global graph
    global ix 
    global iy 
    ix=itemX
    iy=itemY  
    for rec in rectangle:
        #가로선 1로 만들기
        for i in range(2*rec[0],2*rec[2]+1):
            graph[2*rec[1]][i]=1
            graph[2*rec[3]][i]=1
        # 세로선 1로 만들기
        for j in range(2*rec[1],2*rec[3]+1):
            graph[j][2*rec[0]]=1
            graph[j][2*rec[2]]=1

    for i in range(1,20):
        for j in range(1,20):
            for rec in rectangle:
                if 2*rec[0]< j and j<2*rec[2] and 2*rec[1]<i and i<2*rec[3]:
                    graph[i][j]=0
    g=bfs(2*characterY,2*characterX)
    for i in range(19,-1,-1):
        print(g[i])
        # 직사각형 내부를 다 0으로 만들어버려 그 후
    # print(g[16][14])
    
    answer=g[2*iy][2*ix]
    return answer



print(solution([[1,1,5,7]],1,1,4,7))