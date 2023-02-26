#  A 와 B 행렬이 주어지고 A 에 행렬에 3x3 모든 원소를 몇번 바꾸면 B 가 된다
import heapq
def solution():
    N, M = map(int,input().split())
    A=[]
    B=[]
    for _ in range(2*N):
        if _<N:
            A.append(input())
        else:
            B.append(input())
    # 멀쩡한 거 다음 부터 바꿈
    for i in range(N-2):
        if A[i]!=B[i]:
            pass
    print(A)
    print(B)

array=[[4,0],[1,32],[2,74]]
arr=[]
heapq.heapify(array)
print(heapq.heappop(array))
print(heapq.heappop(array))
print(heapq.heappop(array))