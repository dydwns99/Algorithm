# 2138번 전구와 스위치

# 얕은 복사(shallow copy) - a is swt 는 False 지만 , 만약 a안에 객체가 있다면 그 객체들은 메모리 값이 같음
# 깊은 복사(deep copy) - import copy     copy.deepcopy() -> 내부 객체까지 메모리 주소 바꿈


n=int(input())
bulb = list(map(int,input()))
target = list(map(int,input()))


def change(A,B):
    A_copy = A[:]
    press=0
    for i in range(1,n):
        if A_copy[i-1]==B[i-1]:
            continue
        press+=1
        for j in range(i-1,i+2):
            if j<n:
                # ... n-3 n-2 n-1, n-2 n-1, n-1 처럼 끝까지 확인하여 바꿀 수 있음
                A_copy[j]=1-A_copy[j] 
    if A_copy == B:
        return press
    else:
        return 1e9
res = change(bulb, target)

bulb[0]=1-bulb[0]
bulb[1]=1-bulb[1]

res = min(res, change(bulb,target)+1)

if res!=1e9:
    print(res)
else:
    print(-1)

   





