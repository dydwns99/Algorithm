from collections import deque

def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    qa = deque()
    for i in a:
        qa.append(i)
    qb = deque()
    for i in b:
        qb.append(i)
    qc = deque()
    for i in c:
        qc.append(i)
    score={1:0, 2:0, 3:0}
    for ans in answers:
        # [1,4,2,5,2,3,4,4,1....]
        # 각자의 답이 반복되게 하려면,, 큐?
        x = qa.popleft()
        y = qb.popleft()
        z = qc.popleft()
        if ans==x:
            score[1]+=1
        if ans==y:
            score[2]+=1
        if ans==z:
            score[3]+=1
        qa.append(x)
        qb.append(y)
        qc.append(z)
    mx = max(score[1],score[2],score[3])
    res=[]
    for i in range(1,4):
        if mx == score[i]:
            res.append(i)
    print(res)

solution([1,2,3,4,5])

