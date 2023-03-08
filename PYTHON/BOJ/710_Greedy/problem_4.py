# 행렬
n, m = map(int,input().split())
a=[]
b=[]
for i in range(n):
    arr=list(map(int,input()))
    a.append(arr)
for j in range(n):
    arr=list(map(int,input()))
    b.append(arr)
count=0

def change(i,j,array):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if array[x][y]==0:
                array[x][y]=1
            else:
                array[x][y]=0

# 값이 달라진 좌표를 기록하고
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            change(i,j,a)
            count+=1

for i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            count=-1
print(count)

