# 수를 적절히 더하고 빼서 타겟 넘버로 만들어야함

def solution(numbers,target):
    answer=0
    if not numbers and target==0:
        return 1
    if not numbers and target:
        return 0
    return solution(numbers[1:],target-numbers[0])+solution(numbers[1:],target-numbers[0])

    return answer

# bfs, graph queue

