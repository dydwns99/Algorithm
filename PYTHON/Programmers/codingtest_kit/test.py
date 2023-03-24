# 네트워크

# 1 와 2 가 연결되어 있으면
# (1, 1,  ....)
# 아니면
# (1, 0, ...)



def dfs(graph, v, visited):
    visited[v]=True
    for i in range(len(graph[v])):
        if visited[i]==False and graph[v][i]==1:
            dfs(graph,i, visited)



def solution(n,computers):
    count=0
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            dfs(computers,i,visited)
            count+=1
    return count

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        



