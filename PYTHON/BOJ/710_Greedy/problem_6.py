# 1202번 보석 도둑
import heapq
# N : 보석 개수  K : 가방 개수
n, k = map(int, input().split())
# M : 각 보석의 무게  V : 각 보석의 가격 [M, V]
stones=[]
for i in range(n):
    m, v = map(int,input().split())
    stones.append((m, v))
# 가격별로 정리하고
stones.sort(key = lambda x : x[1], reverse=True)
# 가방의 최대 무게
bags=[]
for i in range(k):
    weight = int(input())
    bags.append(weight)

# print("stones : ",stones)
price=0
sum=0
# print("반복문 시작")
for st in stones:
    tmp_bag=[]
    heapq.heapify(bags)
    count=len(bags)
    # print("bags : ", bags)
    while count!=0:
        count-=1
        bag = heapq.heappop(bags)
        # print("bag : ", bag)
        # 처음으로 가방에 보석이 들어가면 그 가방은 다시 쓰지 않고 반복문 나옴
        if bag>=st[0]:
            sum+=st[1]
            # 담지 못했던 가방들을 다시 bags 배열에 넣음
            bags = bags + tmp_bag
            break
        # 가방이 보석을 담지 못한다면
        # 다시 꺼낸 가방을 넣음
        else:
            if count==0:
                bags=tmp_bag
                break
            tmp_bag.append(bag)
        # 모든 가방을 다 확인해 봤다면 반복문 나옴
        
    # print("----")
        
print(sum)



