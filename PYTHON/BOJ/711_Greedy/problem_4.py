# 10610번  30

# 양수 N를 구성하는 숫자들을 섞어 30의 배수가 되는 가장 큰 수

# n : 양수, 10^5개의 숫자로 구성
num = list(input())
num.sort(reverse=True)

sum=0
for n in num:
        sum+=int(n)
if '0' not in num or sum%3!=0:
    print(-1)
else:
    print(int("".join(num)))


