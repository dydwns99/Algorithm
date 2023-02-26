n,m = map(int,input().split())# n=떡의 개수, m= 요청한 떡의 길이
array=list(map(int,input().split()))
# 중간값 찾으면 반환
# 못찾으면 start와 end 를 조정해나감

# end = 젤 큰 떡의 길이, start = 0
start=0
end=max(array)
answer=0
while start<=end:
    total=0
    mid= (start+end)//2
    for x in array:
        if x>mid:
            total+= x-mid
    # 요청한 떡의 길이가 만약 mid 보다 큰곳에 있다면 start값을 조정
    print(mid)
    if m <= total:
        start=mid+1
        answer=mid
    else:
        end=mid-1
print(answer)

