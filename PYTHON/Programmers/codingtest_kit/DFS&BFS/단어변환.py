# 한 개의 알파벳만 바꿔서
# words에 있는 단어로 변환

def solution(begin, target, words):
    answer = 0
    # begin과 비교했을때 한 알파벳만 다른거를 고름
    visited=[False]*len(words)
    find=True
    #words에 target 단어가 없을 경우
    if target not in words:
        find=False
    #words에 target단어가 있을 경우
    while begin != target and find:
        print(begin)
        for idx, word in enumerate(words):
            if compare(begin,target)==1:
                begin = target
                answer+=1
                break
            #한 알파벳만 다를 경우
            if compare(begin,word)==1 and visited[idx]==False:
                visited[idx]=True
                begin=word
                answer+=1
                break

    if find:
        pass
    else:
        answer=0
    return answer

# 한 알파벳만 다른지 확인하는 함수
def compare(x,y):
    count=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            count+=1
    return count
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))