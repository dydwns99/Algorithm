# 가능한 의상 조합 개수 return
# 종류별 하나만, 단 다르개 조합할 경우 가능 조합으로 포함
from itertools import combinations
def solution(clothes):

    # 의상종류를 키 값으로하고
    # 의상 이름을 value값으로 받음
    box = dict()
    for c in clothes:
        box[c[1]]=[]
    for c in clothes:
        box[c[1]].append(c[0])
    # list(dict())하면 키 값만 나오는구나
    # 우선 종류별로 나눴어
    # 그 다음엔 가능한 조합을 만들어야되니까
    # 각 종류의 조합을 구하고
    comb=[]
    for i in range(1,len(box)+1):
        comb.append(list(combinations(list(box),i)))
    # 그 조합주엥서 하나씩 꺼내 개수를 곱합
    count=0
    for com in comb: # 종류 조합이 1개일떄, 2개일때, 3개일때,
        for co in com:
            tmp=1
            for c in co:
                tmp=tmp*len(box[c])
            count+=tmp

    return count

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))