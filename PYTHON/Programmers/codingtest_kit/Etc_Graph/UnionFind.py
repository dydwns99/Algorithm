# 서로소 집합 자료구조 : 기본 구현 방법
# def find_parent(parent,x):
#     if parent[x]!=x:
#         return find_parent(parent,parent[x])
#     return x

# 경로 압축
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

# union연산
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1,v+1):
    print(find_parent(parent, i), end=' ')


print()
# 바로 연결되어 있는 노드, 루트 노드 x
print('부모 테이블: ', end=' ')
for i in range(1,v+1):
    print(parent[i], end=' ')