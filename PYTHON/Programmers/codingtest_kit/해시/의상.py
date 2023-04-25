# 가능한 의상 조합 개수 return
# 종류별 하나만, 단 다르개 조합할 경우 가능 조합으로 포함
from itertools import combinations
def solution(clothes):

    # 의상종류를 키 값으로하고
    # 의상 이름을 value값으로 받음
    count=1
    box = {}
    for c in clothes:
        key = c[1]
        value = c[0]
        if key in box:
            box[key].append(value)
        else:
            box[key] = [value]
    for key in box.keys():
        count = count * (len(box[key])+1)

    return count-1

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))