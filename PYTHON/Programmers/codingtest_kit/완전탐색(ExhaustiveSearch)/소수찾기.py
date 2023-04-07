import itertools
import math
def solution(numbers):
    answer =0
    num = list(numbers)
    # 주어진 문자를 순열하여 소수 인지를 판별
    cmb = []
    for i in range(1,len(num)+1):
        cmb.extend(list(itertools.permutations(num,i)))

    rnw=set()
    for c in cmb:
        tmp = list(c)
        for i in range(len(tmp)):
            if tmp[i]!= 0:
                break
            else:
                tmp.pop(0)
        n = int("".join(tmp))
        rnw.add(n)

    for c in rnw:
        if c == 2 or c == 3:
            answer+=1
        for i in range(2, int(math.sqrt(c)+1)):
            if c % i ==0:
                break
            elif c%i!=0 and i == int(math.sqrt(c)):
                answer+=1
    return answer

print(solution("011"))
# arr = ['A', 'B', 'C']


