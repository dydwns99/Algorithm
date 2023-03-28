#특정한 합을 가지는 부분 연속 수열 찾기 - 투포인터
n=5
m=5
data=[1,2,3,2,5]
count=0
interval_sum=0
end=0


for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum<m and end<n:
        interval_sum+=data[end]
        end+=1
    # 부분합이 m 일 때 카운트 증가
    if interval_sum==m:
        count+=1
    interval_sum-=data[start]