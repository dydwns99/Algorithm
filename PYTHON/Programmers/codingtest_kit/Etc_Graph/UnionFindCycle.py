# 서로소 집합을 활용한 사이클 판별
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    # 작은 쪽의 노드가 부모가 됨
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e = map(int,input().split())
parent=[0]*(v+1) # 부모 테이블

for i in range(1,v+1):
    parent[i]=i

cycle = False

for i in range(n):
    a, b = map(int, input().split())
    # 사이클 발생 경우 종류
    if find_parent(parent, a)==find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)
if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 x")