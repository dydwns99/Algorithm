# 12015번  가장 긴 증가하는 부분 수열 2
# n : 수열의 크기
n = int(input())
# 수열
arr = list(map(int, input().split()))



tmp=[]
tmp[0]=0
for a in arr:
    if tmp[-1] < a:
      tmp.append(a)


    else:
        start = 0
        end = len(tmp)
        while start<end:
            mid = (start+end) // 2    # 1
            if tmp[mid] < a:
                start=mid+1
            elif tmp[mid] >= a:
                end = mid
        tmp[end]=a
print(len(tmp)-1)

    

