# 단속 카메라 
def solution(routes):
    answer=0
    routes.sort(key=lambda x:x[1])
    # print(routes)
    leng = len(routes)
    check =[0]*leng
    
    for i in range(leng):
        # 아직 확인을 안했다면
        if check[i]==0: 
            cam=routes[i][1] # 카메라는 고속도로의 끝에 위치
            answer+=1 # 설치했으므로 카운트 해줌
        for j in range(i+1, leng): # 그 다음 고속도로부터
            if check[j]==0 and routes[j][0]<=cam <=routes[j][1]: # 아직 확인을 안했고 카메라가 그 고속도로 사이에 있다면
                check[j]=1 #확인 체크를 함
    return answer

# 
# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
#     camera = -30001 # -30001부터 카메라 위치를 찾습니다.

#     for route in routes:
#         if camera < route[0]:
#             answer += 1
#             camera = route[1]
#     return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))