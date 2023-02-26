# 11047번 - 동전 0

# 필요한 동전개수의 최솟값

# 입력 줄 N 종류, K원 만들기
# 큰 수 부터 확인하여 나눔
def solution():
    N, K = map(int, input().split())
    arr=[]
    for i in range(N):
        arr.append(input())
    arr.reverse()
    # 나누는 몫이 0이 될때까지 반복
    print("type arr ",type(arr))
    count=0
    for a in arr:
        a=int(a)
        while K!=0:
            if K/a!=0:
                count+=int(K/a)
                K = int(K % a)
                print("K ",K)
            break
    return count

print(solution())
