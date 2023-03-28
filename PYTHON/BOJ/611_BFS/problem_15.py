# 10026번 적록색약
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def can(blind, u, v):
    if u == v:
        return True
    if blind:
        if u == 'R' and v == 'G':
            return True
        if u == 'G' and v == 'R':
            return True
    return False


def bfs(color,blind):
    n = len(color)
    check = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            ans+=1
            q=deque()
            q.append((i,j))
            check[i][j]=True

            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = dx[k]+x
                    ny = dy[k]+y
                    if 0<=nx<n and 0<=ny<n:
                        if check[nx][ny]:
                            continue
                        if can(blind,color[x][y],color[nx][ny]):
                            check[nx][ny]=True
                            q.append((nx,ny))
    return ans
n = int(input())
color = [input() for _ in range(n)]
print(str(bfs(color, False)) + ' ' + str(bfs(color, True)))

