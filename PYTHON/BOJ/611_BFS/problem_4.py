# 14502번  연구소
from collections import deque
# 벽 3개를 세운 뒤, 안전 영역 크기의 최댓값

# 입력값
# n : 세로, m : 가로
n, m = map(int, input().split())
# 연구소
real_lab=[]
for i in range(n):
    real_lab.append(list(map(int, input().split())))
# 2를 발견하면 상하좌우로 1을 만듬
# for l in real_lab:
#     print(l)
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
            if nx<0 or ny<0 or nx>=n or ny>=m or lab[nx][ny]==1 or lab[nx][ny]==2:
                continue
            if lab[nx][ny]==0:
                lab[nx][ny]=2
            q.append((nx,ny))      

# 0 인 곳 3개를 골라 1로 바꿔 봄
loc=[]
for i in range(n):
    for j in range(m):
        if real_lab[i][j]==0:
            loc.append((i,j))
# 0 인 곳 중 3개를 고르는 모든 경우의 수를 다 따짐 -> 최대 64 x 64 x 64
res=0
for a in loc:
    for b in loc:
        for c in loc:
            if a==b or b==c or a==c:
                continue
            lab=real_lab[:]
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
            # bfs(0,0,lab)
            # for la in lab:
            #     print(la)
            # print("------")
            # for t in range(n):
            #     for k in range(m):
            #         if lab[t][k]==0:
            #             count+=1

            res=max(res,count)
print(res)
#   그 다음 2인 곳을 찾고
#   1을 만나기 전까지 2로 바꿈
# 0의 개수를 세고
# 반복하며 최대인 값을 찾암