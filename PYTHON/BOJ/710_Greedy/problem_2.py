# 회의실 배정

# 회의의 수 N / 회의 시간 - 끝
l = int(input())

m = []
for i in range(l):
    a, b = map(int,input().split())
    m.append((a,b))
m.sort(key=lambda x : (x[1], x[0])) # 애초에 정렬을 회의의 끝나는 시간을 오름차순해야 연속 가능한 회의 수를 카운트 할 수 있음

end = m[0][1]
count = 1
for i in range(1, len(m)):
    if end <= m[i][0]:
        count += 1
        end = m[i][1]
print(count)
