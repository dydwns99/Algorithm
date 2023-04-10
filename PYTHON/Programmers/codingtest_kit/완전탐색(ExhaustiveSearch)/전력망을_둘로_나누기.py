# 나눴을 때 두개의 송전탑의 개수가 최대한 비슷해야함
from collections import Counter
def findParent(parent,x):
    if parent[x]!=x:
        parent[x]=findParent(parent,parent[x])
    return parent[x]
        

def union(parent,x,y):
    x = findParent(parent,x)
    y = findParent(parent,y)

    if parent[x]>y:
        parent[x]=y
    elif x<y:
        parent[y]=x


def solution(n, wires):
    # 송전탑을 어떻게 나눠야 되나?
    # 노드들의 부모노드는 일단 자기 자신으로 초기화
    parent=[0]*(n+1)

    # parent = [1,2,3,4,5,6,7,8,9]
    ans=float('inf')
    for i in range(len(wires)):
        for j in range(1,n+1):
            parent[j]=j

        cp = wires[:]
        cp.pop(i)

        for wire in cp:
            if findParent(parent,wire[0]) == findParent(parent,wire[1]):
                continue
            union(parent,wire[0],wire[1])


        uf = []
        for i in range(1, n + 1):
            uf.append(findParent(parent,i))
            
        uf = Counter(uf)
        print("uf ",uf)
        v = list(uf.values())
        print("v ",v)
        ans= min(ans, abs( v[0]- v[1]))
    print(ans)

    return ans

solution(9,	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])