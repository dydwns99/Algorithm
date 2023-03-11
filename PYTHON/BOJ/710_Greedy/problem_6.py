# 1202번 보석 도둑
# N : 보석 개수  K : 가방 개수
n, k = map(int, input().split())
# M : 각 보석의 무게  V : 각 보석의 가격 [M, V]
stones=[]
for i in range(n):
    m, v = map(int,input().split())
    stones.append((m, v))
# 가격별로 정리하고
stones.sort(key = lambda x : x[1], reverse=True)
# 그후 무게 별로
# print("stones : ",stones)
# 가방의 최대 무게
c=[]
for i in range(k):
    weight = int(input())
    c.append(weight)
# print("c : ",c)
price=0
sum=0
# 가격이 제일 비싼 보석을 , 한계 무게가 최대한 타이트한 가방에 넣음
# 10^10 이 최대 시간이므로 좀 줄여야함
# 한계 무게가 최대한 타이트한 가방을 찾으려면,,, 
for st in stones:
    # 그 가방 배열에 해당 보석의 무게 값을 넣어 정렬시킨 후
    # 정렬된 배열에서 그 보석 인덱스의 바로 앞 인덱스를 추출함
    # 그 인덱스의 가방은 사용했으므로 제거 + 보석도 제거
    c.append(st[0])
    c.sort()
    print("c : ",c)
    idx = c.index(st[0]) # 보석의 인덱스 값
    print("idx : ",idx)
    if  k>0:
        # 만약 같다면 idx 값만 제거하면됨
        if st[0]==c[idx+1]:
            c.remove(c[idx])
            c.remove(c[idx])
        if st[0]<c[idx+1]:
            #사용한 가방제거
            c.remove(c[idx+1])
            #넣었던 보석제거
            c.remove(c[idx])
        price=st[1]
        k-=1
        sum+=price
        
print(sum)



