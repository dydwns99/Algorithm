# 1080번 행렬
# n x m 행렬
n, m = map(int, input().split())
# 행렬 a 와 행렬 b
a=[]
for i in range(n):
    tmp = list(map(int, input()))
    a.append(tmp)
b=[]
for i in range(n):
    tmp = list(map(int, input()))
    b.append(tmp)
# a 에서 b 로 바꿀 수 있다면 몇번 뒤집어야하는지 출력
# 바꿀 수 없다면 -1 출력

# 연산 - 3x3 크기의 부분 행렬에 있는 모든 원소를 뒤집는다

# 첫번째 행부터 같은지 안같은지 확인 한후 
# 안같으면 연산 수행
# print("a:")
# for i in range(n):
#     print(a[i])
# print("b:")
# for i in range(n):
#     print(b[i])
count=0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            # 연산 수행
            count+=1
            for t in range(i,i+3):
                for k in range(j,j+3):
                    a[t][k]=1-a[t][k]
# print("after a ")
# for i in range(n):
#     print(a[i])
for i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            count=-1
            break

print(count)
