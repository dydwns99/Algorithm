# N 여러개로 사칙연산을 수행하여 number 만들고 사용한 N의 개수의 최솟값 출력
def solution(N,number):
    ############## => 1개, 2개, ... 8개 까지 경우를 모두 구하면서 number 찾음
    
    # 1개로 만드는 값들을 배열에 담고 -> 그 전의 makenums의 모든 원소에 대해 N을 / * + - 연산함
    # number가 있는지 확인, 
    # 있으면 개수 반환
    # 없으면 2개로 넘어감,

    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    for i in range(8): # 4
        for j in range(i): # 0,1,2,3
            for num1 in dp[j]: # dp[0], dp[1], dp[2], dp[3]
                for num2 in dp[i-j-1]: # dp[3], dp[2], dp[1], dp[0]
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    dp[i].add(num1*num2)
                    if num2!=0:
                        dp[i].add(num1//num2)
        if number in dp[i]:
            return i+1
    return -1

print(solution(5,12))
