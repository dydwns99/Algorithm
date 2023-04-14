# 내가 인쇄를 요청한 문서가 몇번째로 인쇄되는지 리턴
from collections import deque
def solution(priorities, location):
    #location 인덱스를 가진 원소가 몇번째로 인쇄되나?
    # ['A','B','C','D',..]을 만들고 중요도를 매핑해줌
    # 나갈때마다 count+=1
    # 만약 나가는게 location에 있는 문서면 count 반환하고 끝냄

    paper =dict()
    for idx, p in enumerate(priorities):
        paper[str(idx)]=p
    q=deque()
    for p in list(paper.keys()):
        q.append(p)
    count=0
    res=0
    # 현재 키값들이 큐에 들가 있음
    while q:
        key = q.popleft()
        # 그 키 값을 제외한 키값들의 value값들 중 최대값
        mx=0
        for k in q:
            if mx<=paper[k]:
                mx=paper[k]
        
        if paper[key]>=mx:
            count+=1
            if int(key)==location:
                res=count
                break
        else:
            q.append(key)

    return res

solution([1, 1, 9, 1, 1, 1],0)

