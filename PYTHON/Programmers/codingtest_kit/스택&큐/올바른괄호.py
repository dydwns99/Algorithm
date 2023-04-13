# 올바른 괄호인지를 구분하여 return

def solution(s):

    # 첫 괄호 보냄
    # ((
    answer=True
    stg = []
    for i in s:
        if i=='(':
            stg.append(i)
        elif i==')':
            if stg:
                stg.pop()
            else:
                stg.append(i)
    if stg:
        answer=False

    return answer
solution("(()(")
