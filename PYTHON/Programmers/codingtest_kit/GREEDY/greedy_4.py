# 구명보트를 최대한 적게
# 순서가 필요 없고 한 보트에 최대한 많은 인원이 들어 가야 함 ->
# 가장 무게 많이 나가는 사람이랑 가장 적게 나가는 사람 합쳐서 판별 -> 그래야 과체중이라도 포함할 수 있기 때문!
# 최대 2명인걸 간과함
def solution(people, limit):
    people.sort()
    arr = []
    answer=0
    for p in people:
        arr.append(p)
        while arr:
            if sum(arr) < limit:
                break
            elif sum(arr) == limit:
                arr.clear()
                answer += 1
            elif sum(arr) >= limit:
                arr.clear()
                answer += 1
                arr.append(p)
                print(arr)
    if arr:
        answer+=1
    return answer
print(solution([70, 80, 50],100))

# 다른 사람 풀이

##
# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer
