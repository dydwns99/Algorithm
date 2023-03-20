# 1541번  잃어버린 괄호
import sys
# 괄호 쳐서 식의 값을 최소로 만들기

# 식을 문자열로 입력 받고
arr = list(sys.stdin.readline().strip().split('-'))
#  - 뒤에 수를 가장 큰 수로 만들어야함
cal = sum(list(map(int,arr[0].split('+'))))
# 첫번째 원소는 무조건 + , 나머지 모두 -
if len(arr)==1:
    print(cal)
else:
    for i in range(1,len(arr)):
        sub=sum(list(map(int,arr[i].split('+'))))
        cal-=sub
    print(cal)