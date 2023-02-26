from string import ascii_uppercase
def solution(name):
    # 각 스펠링과 A와의 거리차를 파악
    alpha_dic={}
    answer = 0
    for i in ascii_uppercase:
        if ord(i)>=78:
            alpha_dic[i] = 26-abs(ord('A')-ord(i))
        else:
            alpha_dic[i]= abs(ord('A')-ord(i))
    # 그리고 단어 입력 받고 거리차 합계 저장
    for c in name:
        answer+=alpha_dic[c]
    # 조이스틱 좌우 이동
    n=len(name)
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        # A가 아닌 다른 알파벳 발견할 때 까지 ~
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx) # idx는 오른쪽 방향으로 이동한 칸 / n-next_idx = 왼쪽 방향으로 이동한칸
        move = min(move, idx + n - next_idx + distance)
    answer += move
    return answer
#


