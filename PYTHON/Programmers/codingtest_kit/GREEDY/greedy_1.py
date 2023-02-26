
# 오늘의 배운점 : 리스트안에 있는 원소들을 for문을 사용해 제거할때는
#참조할 때는 리스트 복사본을 삭제할 때는 리스트 원본을 사용해야한다.
# 참조할 때 원본을 쓸 경우 모든 원소가 삭제 되지 않음 -> remove()는 특정 원소를
# 삭제하는 것이지만 인덱스와 연관이 있어 보임!!
def solution1(n,lost,reserve):
    #먼저 여벌 있는데 도난 당한 사람들 판별 -> 빌려줄 수 없기 때문
    re=reserve
    lo=lost
    for r in re[:]:
        print("밖 r")
        print(r)
        if r in lo[:]:
            print(r)
            lost.remove(r)
            reserve.remove(r)
            print(str(lost))
            print(str(reserve))
    answer = n - len(lost)
    # 정렬
    lost.sort()
    reserve.sort()
    #최대한 많이 옷을 빌려주려면 -> 빌려주는 방향이 겹치면 안됨
    for r in reserve:
        #끝의 학생 먼저 여벌있으면 빌려줌
        if r-1 in lost:
            answer+=1
            lost.remove(r-1)
        else:
            if r+1 in lost:
                answer+=1
                lost.remove(r+1)
    return answer
print(solution(8,[8,5,2,3,1],[4,5,2]))
