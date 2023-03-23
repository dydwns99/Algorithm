# DFS
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph,i,visited)