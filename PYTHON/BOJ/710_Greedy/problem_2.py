# 1931번
# 최대 사용할 수 있는 회의의 최대 개수
# 1부터 시작될 수도 있고 , 중간부터 시작될 수도 있음
# 시작시간과 끝시간이 가장 작은것을 선택


# def solution():
#     N = int(input())
#     time=[]
#     for _ in range(N):
#         s, e = map(int, input().split())
#         time.append([s,e])
#
#     time=sorted(time,key=lambda  a: a[0])
#     time=sorted(time, key=lambda  a: a[1])
#
#     last =0
#     count =0
#
#     for i, j in time:
#         if i>=last:
#             count+=1
#             last=j
#     return count
# solution()

