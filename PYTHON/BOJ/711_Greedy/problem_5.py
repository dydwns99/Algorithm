# 1783번  병든 나이트

# N : 세로, M : 가로
n, m = map(int,input().split()) # n=17 m=5
# 병든 나이트가 여행에서 방문할 수 있는 칸 개수 중 최댓값
move=0
# 방문 5칸이상 부터는 이동방법 한번씩은 사용!
    # 가로 >= 7  and 세로 >= 3
if m >= 7 and n >= 3:
    # 이동방법 -> 일단 1-4-2-3 으로 시작
    move+=4
    #        -> 그후 가로수 만큼 이동 가능
    move += m-7
# 4칸 이하일 경우 
    # 가로 <7 or 세로 <3
elif m<7 or n<3:
    #   세로 1 -> 1
    if n==1:
        pass
    #   세로 2 -> 가로 >= 3 부터 이동 가능
    elif n==2 and m>=3:
        if m%2!=0:
            move += m//2
        else:
            move += m//2 -1
    #   세로 3이상 -> 가로 >= 2 부터 이동 가능
    elif n>=3 and m>=2:
        move +=m-1
    move = min(3,move)

res=move+1
print(res)
# 세로가 더 길 경우
#   가로 길이만큼 이동가능 

#  가로가 더 긴 경우


# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# 0 0 1 0 0


