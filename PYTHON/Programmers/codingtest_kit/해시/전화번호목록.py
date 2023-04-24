# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 그렇지 않으면 true를 return하도록
def solution(phone_book):

    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])]== phone_book[i]:
                answer=False
                break
    return answer