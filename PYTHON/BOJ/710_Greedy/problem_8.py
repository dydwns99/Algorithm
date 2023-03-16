# 2109번  순회강연
import heapq
# n : 대학 수
n = int(input())
# d : 강연 기한   p : 강연료
univ=[]
mx=0
for i in range(n):
    p, d = map(int, input().split())
    if d>=mx:
        mx=d
    univ.append((p, d))
# 최대로 벌 수 있는 돈, 
# 기한 날짜 오름차순
univ.sort(reverse=True) # 강연료 큰 대학 부터 로직 들어감
ans=0
visited=[0] * (mx+1) # 방문한 날짜
for p, d in univ:
    for i in range(d,0,-1):
        if not visited[i]: # 방문했다면 기한 내에 방문안한 날짜에 등록
            visited[i]=1
            ans+=p
            break
    

