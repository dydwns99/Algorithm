
# 14502번  연구소
from collections import deque
import copy
# 벽 3개를 세운 뒤, 안전 영역 크기의 최댓값

# 입력값
# n : 세로, m : 가로
n, m = map(int, input().split())
# 연구소
real_lab=[]
for i in range(n):
    real_lab.append(list(map(int, input().split())))

# bfs 함수

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y,lab):
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if lab[nx][ny]==0:
                lab[nx][ny]=2
                q.append((nx,ny))      

# 0 인 곳 3개를 골라 1로 바꿔 봄
loc=[]
vir=[]
for i in range(n):
    for j in range(m):
        if real_lab[i][j]==0:
            loc.append((i,j))
        if real_lab[i][j]==2:
            vir.append((i,j))
# 0 인 곳 중 3개를 고르는 모든 경우의 수를 다 따짐 -> 최대 64 x 64 x 64
res=0
for a in loc:
    for b in loc:
        for c in loc:
            if a==b or b==c or a==c:
                continue
            lab=copy.deepcopy(real_lab)
            count=0
            # print("a",a)
            # print("b",b)
            # print("c",c)
            x1,y1 = a
            x2,y2 = b
            x3,y3 = c
            lab[x1][y1]=1
            lab[x2][y2]=1
            lab[x3][y3]=1

            for i,r in vir:
                bfs(i,r,lab)


            for t in range(n):
                for k in range(m):
                    if lab[t][k]==0:
                        count+=1

            res=max(res,count)
print(res)

# 백준 풀이

# from collections import deque
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# def bfs(a):
#     n = len(a)
#     m = len(a[0])
#     b = [[0]*m for _ in range(n)]
#     q = deque()
#     for i in range(n):
#         for j in range(m):
#             b[i][j] = a[i][j]
#             if b[i][j] == 2:
#                 q.append((i,j))
#     while q:
#         x,y = q.popleft()
#         for k in range(4):
#             nx,ny = x+dx[k], y+dy[k]
#             if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
#                 b[nx][ny] = 2
#                 q.append((nx,ny))
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if b[i][j] == 0:
#                 cnt += 1
#     return cnt

# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# ans = 0
# for x1 in range(n):
#     for y1 in range(m):
#         if a[x1][y1] != 0:
#             continue
#         for x2 in range(n):
#             for y2 in range(m):
#                 if a[x2][y2] != 0:
#                     continue
#                 for x3 in range(n):
#                     for y3 in range(m):
#                         if a[x3][y3] != 0:
#                             continue
#                         if x1 == x2 and y1 == y2:
#                             continue
#                         if x1 == x3 and y1 == y3:
#                             continue
#                         if x2 == x3 and y2 == y3:
#                             continue
#                         a[x1][y1] = 1
#                         a[x2][y2] = 1
#                         a[x3][y3] = 1
#                         cur = bfs(a)
#                         if ans < cur:
#                             ans = cur
#                         a[x1][y1] = 0
#                         a[x2][y2] = 0
#                         a[x3][y3] = 0
# print(ans)
