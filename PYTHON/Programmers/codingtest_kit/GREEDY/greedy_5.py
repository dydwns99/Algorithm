import heapq
# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x: x[2]) 
#     link = set([costs[0][0]])

#     # Kruskal 알고리즘으로 최소 비용 구하기
#     while len(link) != n:
#         for v in costs:
#             if v[0] in link and v[1] in link:
#                 continue
#             if v[0] in link or v[1] in link:
#                 link.update([v[0], v[1]])
#                 answer += v[2]
#                 break
                
#     return answer

#크루스칼 알고리즘

#부모 노드를 찾아줌
def ancestor(parents,node):
    if parents[node] == node:
        return node
    else:
        return ancestor( parents,parents[node])
def union(parents,a,b):
    x=ancestor(parents,a)
    y=ancestor(parents,b)
    if x==y:
        return
    else:
        if x<y:
            parents[y]=x
        elif x>y:
            parents[x]=y
        return parents

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        #부모가 같지 않다면 -> 같은 사이클이 아님
        if ancestor(parents,f) != ancestor(parents,t):
            answer += w
            # 부모 관계로 설정해 둘을 그룹으로 묶어줌
            union(parents,f,t)
            # parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    print("parents : ", parents)
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


        

    
