# 2109번 순회강연

#가장 많은 돈을 벌 수 있도록
n = int(input()) # 대학 수
# d일 안에 아무 때나 강연을 할 수 가 있다.
# 단, 하루에 하나씩

# 각 대학의 d(기한) p(강연료) 튜플
univ=[]
mx=0
time=[[]*6 for _ in range(6)]
for i in range(n):
    p, d = map(int, input().split())
    if d>=mx:
        mx=d
    univ.append((p, d))

univ.sort(reverse=True)
# print(univ)
# # 여기서 부턴 가장 큰 수 부터 차례로 
visited=[0]* (mx+1)
ans=0
for p, d in univ: # 내림차순이므로 처음 p 는 가장 큰 돈
    for i in range(d,0,-1): # day에 -1 을 해가며 방문안한 날짜를 차례대로 큰돈이 되는 대학 순으로 집어 넣을 수 있음
        if not visited[i]:
            visited[i]=1
            ans+=p
            break
print(ans)




