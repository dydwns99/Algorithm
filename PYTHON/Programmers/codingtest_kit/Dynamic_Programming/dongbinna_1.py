# 얻을 수 있는 식량의 최댓값, 단 약탈 시 인접해 있으면 안됨

n = int(input())
storage=list(map(int, input().split()))
# an = max(an-2 + an , an-1)
d=[0]*n
d[0] = storage[0]
d[1] = max(storage[0], storage[1])
# 그다음 d[2] 부터 시작
for i in range(2,n):
    d[i]=max(d[i-2]+storage[i], d[i-1])
print(d[n-1])