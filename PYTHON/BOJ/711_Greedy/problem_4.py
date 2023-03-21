# 10610번  30
import sys
# 양수 N를 구성하는 숫자들을 섞어 30의 배수가 되는 가장 큰 수

# n : 양수, 10^5개의 숫자로 구성
num = list(input())
num.sort(reverse=True)
# 숫자들의 위치를 어떻게 바꿔가며 30 인것을 확인할꺼냐 -> 
max_num="".join(num)
x = int(max_num)//30
# print(num)
# print("x : ",x)
# 몫을 -1 해가며 30의 배수가 있는지 확인
out=-1
for i in range(x,-1,-1):
    tmp = list(str(30 * x))
    res=tmp[:]
    # print("tmp : ",tmp)
    # tmp를 구성하는 숫자들이 num에 전부 존재한다면 출력
    for n in num:
        if n in tmp:
            # print('remove')
            tmp.remove(n)
        else:
            break
        # print("remain tmp : ",tmp)
    if not tmp:
        out = int("".join(res))
        # print(out)
        # print("success! ")
        break
print(out)


