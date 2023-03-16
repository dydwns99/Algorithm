# 1285번 동전 뒤집기

import sys;
input=sys.stdin.readline
def solve():
    N = int(input())
    coins = [0] * N
    for i in range(N):
        # zip() -> 튜플로 묶어줌, 병렬 처리 가능
        # strip() -> 공백 없이 입력 받기
        # (2,H)  /  (1,H)  /  (0,T)   -> 이런 식으로  
        # T 일 때 1로 만들어 주기 위함
        for j, c in zip(range(N-1,-1,-1),input().strip()):
            if c=='T':
                coins[i] += (1<<j)
    print(coins)
    answer=N*N
    # 뒤집을 수 있는 모든 경우의 수
    # 열을 바꾸는 순간 행들의 앞면, 뒷면 개수들은 이미 정해짐으로 건들 필요가 없음
    # 그냥 열을 바꾸면서 개수가 적은 것을 더해가면 그걸로 결정됨
    for flip in range(1<<N): # 0 일 때
        result =0
        for i in range(N):  # 0 1 2
            # bin() -> 십진수를 이진수로 바꿔줌 ,  다르면 1로  같으면 0 으로
            T = bin(coins[i]^flip).count('1') # 특정 열을 뒤집었을 때의 뒷면의 개수
            result += min(T, N-T) # 앞 뒤 면 개수 중 적은 걸 더함
        answer = min(answer, result)
    print(answer)
solve()