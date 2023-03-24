# 16948번  데스나이트
from collections import deque
# r1,c1 에서 r2,c2로 이동하는 최소 이동 횟수
n = int(input())

r1,c1,r2,c2 = map(int, input().split())

dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]

graph=[[0] * n for _ in range(n)]
visited=[[False]*n for _ in range(n)]

def bfs(x, y):
    q=deque()
    q.append((x,y))
    while q:

        x,y = q.popleft()
        for i in range(6):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or visited[nx][ny]==True:
                continue          
            if graph[nx][ny] == 0: 
                graph[nx][ny] = graph[x][y]+1
                visited[nx][ny]=True
            if graph[nx][ny] != 0:
                graph[nx][ny] = min(graph[nx][ny], graph[x][y]+1)
                visited[nx][ny]=True
            if nx==r2 and ny ==c2:
                # print("정답")
                print(graph[r2][c2])
                q.clear()
                break
            q.append((nx,ny))
bfs(r1,c1)
if graph[r2][c2]==0:
    print(-1)


