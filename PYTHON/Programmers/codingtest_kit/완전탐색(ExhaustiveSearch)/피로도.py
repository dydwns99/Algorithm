# 탐험할 수 있는 최대 던전 수
# 최소 필요 피로도, 소모 피로도
import itertools
# 모든 경우 다 고려하여?
def solution(k, dungeons):

    
    test=dungeons[:]
    arr = list(itertools.permutations(test,len(test)))

    res=0
    for ar in arr:
        count=0
        pero=k
    
        print(ar)
        for a in ar:
            if a[0]<=pero:
                pero-=a[1]
                count+=1
            else:
                break
    
        res=max(count, res)
 
    return res
print(solution(80,[[80, 20], [50, 40], [30, 10]]))