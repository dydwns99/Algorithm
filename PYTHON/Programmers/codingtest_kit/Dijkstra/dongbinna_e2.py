import heapq
# 오름차순 힙 정렬
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 내림차순 힙 정렬
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


# 다익스트라 :개선된
#최단거리가 가장 짧은 노드를 선택하기 위해 힙(heap) 자료구조를 이용

