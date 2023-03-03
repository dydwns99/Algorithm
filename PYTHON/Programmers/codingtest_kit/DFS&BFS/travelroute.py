# # 공항 경로를 return, 항공권 모두 사용
# group=[]
# # used[] 생성
# used=[]
# # 모든 경로들을 담은 배열
# routes=[]
# #
# rout=[]
# def dfs(start, used, order, route):
#     global routes
#     # global rout
#     # 시작이 icn인 티켓들을 가져옴
#     for i in range(len(group)): 
#         if used[i]==True and group[i]!=group[order]:
#             if False in used:
#                 return
#             # 모든 used가 True이면 배열 리턴
#             else:
#                 return routes
#         if used[i]==False and group[i][0]==start:
#             used[i]==True;
#             # route.append(group[i]) # 경로 하나하나
#             dfs(group[i][1],used,i,route)

# def solution(tickets):
#     # group , dfs, 재귀
#     global group
#     group=tickets
#     global used
#     used=[False]*len(group)

#     print(dfs("ICN",used,0,[]))
#     answer=[]
#     return answer

# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

from collections import defaultdict


def solution(tickets):
    path = []

    # 1. {시작점: [도착점리스트]} 형태로 그래프 생성
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    # 2. 도착점 리스트를 역순 정렬
    for airport in graph:
        graph[airport].sort(reverse=True)

    # 3. 출발지는 항상 ICN이므로 stack에 먼저 넣어두기
    stack = ["ICN"]
    # 4. DFS로 모든 노드 순회
    while stack:
        # 4-1. 스택에서 가장 위의 저장된 데이터 꺼내오기
        top = stack.pop()

        # 4-2. top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장
        if top not in graph or len(graph[top]) == 0:
            path.append(top)
        # 4-3. top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    # 5. path를 뒤집어서 반환
    return path[::-1]       