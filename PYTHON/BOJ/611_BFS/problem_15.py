# 10026번 적록색약
import copy
n = int(input())
color=[]
for i in range(n):
    color.append(list(input()))
# for c in color:
#     print(c)

visited=[[False]*n for _ in range(n)]
visited2=[[False]*n for _ in range(n)]

def dfs(x,y,col):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if visited[x][y]==False and color[x][y]==col:
        visited[x][y]=True
        dfs(x-1,y,col)
        dfs(x+1,y,col)
        dfs(x,y-1,col)
        dfs(x,y+1,col)
        return True
    # 0,0 부터 시작
    # 0,0 의 색이 R이라면 
    # 상하좌우를 살펴가며 R인 타켓을 방문표시함
    # 다 방문 했으면 count+=1
count=0
for i in range(n):
    for j in range(n):
        col=color[i][j]
        if dfs(i,j,col)==True:
            count+=1
# print("count : ",count)

color2=copy.deepcopy(color)
for i in range(n):
    for j in range(n):
        if color2[i][j]=='R' or color2[i][j]=='G':
            color2[i][j]='S'
# for c in color2:
#     print(c)

def dfs2(x,y,col):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if visited2[x][y]==False and color2[x][y]==col:
        visited2[x][y]=True
        dfs2(x-1,y,col)
        dfs2(x+1,y,col)
        dfs2(x,y-1,col)
        dfs2(x,y+1,col)
        return True

count2=0
for i in range(n):
    for j in range(n):
        col=color2[i][j]
        if dfs2(i,j,col)==True:
            count2+=1
# print("count2 : ",count2)
print(count,count2)
    
