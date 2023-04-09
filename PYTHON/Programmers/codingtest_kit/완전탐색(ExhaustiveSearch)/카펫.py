def solution(brown, yellow):
    # 전체 넓이
    total = brown+yellow
    # 카펫의 가로와 세로 크기를 순서대로 배열에 담아 return
    # 노랑색 직사각형의 
    # 세로가 1일때,
    # 세로가 2일때,
    # 세로가 3일때
    # -> brown을 다 사용할 수 있는지
    res=[]
    for i in range(1,yellow+1):
        if yellow%i!=0:
            continue
        x = int(yellow / i )# 노랑 가로 길이 
        y = i # 노랑 세로 길이
        # 둘러싸인 길이
        tx = x+2
        ty = y+2
        if tx*ty == total:
            res.append(tx)
            res.append(ty)
            break

    return res
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))