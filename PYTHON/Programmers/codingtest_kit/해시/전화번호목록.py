# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 그렇지 않으면 true를 return하도록
def solution(phone_book):
    has=dict()
    for p in phone_book:
        has[p]=0
    # 아니면 1~9 체크
    # 1로 시작하는거 외에 제거
    pb=phone_book[:]
    tmp=[]
    # j 인덱스 위치의 수를 확인
    for j in range(10):   
        for i in range(1,10):
            for p in pb:
                if p[0]==i: # 첫번째 번호가 i로 시작하면
                    tmp[i].append(p)

    
    answer = True
    return answer