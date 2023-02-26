# 11399 번

def solution():
    N = int(input())
    p = input().split()
    for i in range(N):
        p[i]=int(p[i])
    p.sort()
    sum=0
    ans=0
    arr=[]
    for i in range(N):
        sum+=p[i]
        arr.append(sum)
        ans+=sum

    return ans
print(solution())


    # for i in range(N):
    #     arr.append([i+1,p[i]])
    # print(arr)

solution()