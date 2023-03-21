# 2875번  대회 or 인턴

# 최대의 팀 수 구하기
# 팀구성은 무조건 여학생 2 , 남학생 1

# n : 여학생 수 , m : 남학생 수 , k : 인턴쉽
n, m, k = list(map(int, input().split()))

# n, m 에서 k 명을 빼고
# 남은 사람 중에서 조합하여 팀 생성

# n, m 에서 k를 적절하게 어떻게 빼야하나 -> 
tn = n//2 # 여자 팀의 수
tm = m  # 남자 팀의 수
total = min(tn, tm) # 일단 k 생각 말고 팀 만듬
rest = (tn-total)*2 + (tm-total) # 나머지 사람 수
# 만약, 남은 수 < k 이면 
if rest < k :
    #   k - 남은 수 가 1,2,3 일때 전체 팀에서 1빼고
    #   k - 남은 수 가 4,5,6 일때 전체 팀에서 2빼고 
    #   ...
    tmp = k - rest
    a = tmp//3
    if tmp%3 > 0:
        total-=1
    total-=a
print(total)


