
def solution(routes):
    answer=0
    roads = sorted(routes, key= lambda x : x[0])
    # print(roads)
    # 다 더해
    count=0
    while roads:
        cam_loc=dict()
        for i in range(roads[0][0], roads[len(roads)-1][1]+1):
            cam_loc[str(i)]=0

        group = roads
        for road in roads:
            for loc in range(road[0], road[1]+1):
                cam_loc[str(loc)]+=1
        mxidx = max(cam_loc, key=cam_loc.get)
        #가장 높은 수를 빼 -> 그 인덱스에 속한 모든 routes는 뺌 
        # print(mxidx)
        arr=[]
        for road in roads:
            if int(mxidx) in range(road[0], road[1]+1):
                arr.append(road)
                # print(road)
        for r in arr:
            roads.remove(r)
        # print(roads)
        count+=1
    # print(count)
    answer=count
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))