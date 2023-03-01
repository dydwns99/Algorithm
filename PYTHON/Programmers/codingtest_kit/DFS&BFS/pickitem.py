from collections import deque
graph=[]
ix=0
iy=0
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
            if nx<0 or nx>= len(graph) or ny<0 or ny>=len(graph):
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
            elif graph[nx][ny]>1 and nx==iy and ny==ix:
                graph[nx][ny]=min(graph[nx][ny], graph[x][y]+1)
    
    return graph


def solution(rectangle,characterX,characterY,itemX,itemY):
    size=101
    global graph
    graph=[[0]*size for _ in range(size)]
    global ix
    global iy
    ix=2*itemX
    iy=2*itemY
    # 길이 두배로
    for rec in rectangle:
        for i in range(len(rec)):
            rec[i]=2*rec[i]
        
    
    for i in range(size):
        for j in range(size):
            # 가로 선분 사이에 있고 , 세로 선분 사이에 있으면 1
            for rec in rectangle:
                if i>= rec[1] and i<= rec[3] and j>=rec[0] and j<=rec[2]:
                    graph[i][j]=1
            # 직사각형 내부도 모두 0 으로
            for rec in rectangle:
                if i> rec[1] and i< rec[3] and j>rec[0] and j<rec[2]:
                    graph[i][j]=0
    g=bfs(2*characterY,2*characterX)
    # for i in range(39,-1,-1):
    #     print(g[i])
    # print(g[iy][ix])
    return g[iy][ix]//2

print(solution([[1,1,5,7]],1,1,4,7))
