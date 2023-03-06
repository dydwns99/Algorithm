# 판매원이 회사 사이를 이동하게 되는 최소 시간 계산
# n : 회사 개수, m : 경로 개수
INF=int(1e9)
n, m = map(int, input().split())
road=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            road[a][b]=0
for _ in range(m):
    a, b = map(int, input().split())
    road[a][b]=1
    road[b][a]=1
# k먼저 방문하고 x감
x, k = map(int,input().split())
# start 가 1일 때 distance[k] 구한 후
# start 가 k일 때 distance[x] 구함
# 플로이드 워셔 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            road[a][b]= min(road[a][k]+road[k][b], road[a][b])
distance = road[1][k]+road[k][x]
if distance >=INF:
    print("-1")
else:
    print(distance)


