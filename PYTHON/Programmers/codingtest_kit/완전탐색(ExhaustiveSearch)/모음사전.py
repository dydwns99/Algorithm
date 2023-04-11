# 이 단어가 사전에서 몇번쨰 단어인지

def order(n):
    res=0
    for i in range(1,n+1):
        res+=5**i
    return res

def solution(word):
    # 많으면 많을 수록 큰거
    # 그 중에서 AE
    # 만약 첫번째 자리가 E 라면 그 이전의 문자열들의 개수 -> 
    # A + 5 + 5*5 + 5*5*5 + 5*5*5*5 (AUUUU) + E + `` (EUUUU) + I
    l = 5
    count=0
    for w in word:
        l-=1
        if w=='A':
            count+=1
        if w=='E':
            count+= 1+1*(order(l)+1)
        if w=='I':
            count+= 1+2*(order(l)+1)
        if w=='O':
            count+= 1+3*(order(l)+1)
        if w=='U':
            count+= 1+4*(order(l)+1)    

    return count

solution("EIO")


