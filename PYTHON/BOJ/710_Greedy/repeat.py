# 1931번  회의실 배정
# n: 회의의 수
n = int(input())
# 회의 시작시간 , 끝나는 시간
meetings=[]
for i in range(n):
    s,e = map(int, input().split())
    meetings.append((s,e))
# 최대 사용할 수 있는 회의의 최대 개수, 회의 겹치면 안됨

# (1,4) (5,9) (12,14)
# 시작이 작은 숫자 중에서 끝나는 시간 가장 작은 수
meetings.sort(key = lambda x : (x[1],x[0]))
print(meetings)
# 첫 회의 끝나고 다음 회의 정할 때 
# 현재 회의 끝나는 시간 < 다음 회의 시작시간 
count=1
end = meetings[0][1]
for i in range(1, len(meetings)):
    if end <= meetings[i][0]:
        count+=1
        end = meetings[i][1]
print(count)