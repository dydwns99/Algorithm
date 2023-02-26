#  한 노드씩 확인하면서 방문 안되어 있으면 visited=true로 하고 재귀로 다시 들어감
#index 는 자기 자신 인덱스
def dfs(node, computers,visited):
    visited[node]=True
    for i, nei in enumerate(computers[node]):
        if nei>0 and i!=node and visited[i]==False:
            dfs(i,computers,visited)
    return visited


def solution(n,computers):
    visited=[False]*n
    startnode=0
    count=1
    while True:
        visited=dfs(startnode,computers,visited)
        if False in visited:
            startnode=visited.index(False)
            count+=1
        else:
            break
    print(count)

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])


