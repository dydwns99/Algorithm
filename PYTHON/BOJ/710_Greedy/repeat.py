# 2138번  전구와 스위치
# n : 스위치 및 전구의 개수
n = int(input())
# 전구의 현재 상태  -> 0 - 켜져있는   1 - 꺼져있는
a = list(map(int,input()))
# 전구의 나중 상태 (만들고자하는)
b = list(map(int,input()))
# 최소 몇번 눌러야 a에서 b 로 바뀌는지 횟수 출력, 불가능하면 -1 출력
# i 번 스위치 누르면 i-1, i, i+1 이 바뀜

# 맨 왼쪽 수 가 같은 걸 확인하고 다음으로 넘어가야함

# 하지만 첫번째를 누르냐 안누르냐를 결정해야 위 규칙 적용 가능
a1=a[:]
a2=a[:]
ans=[]
for t in range(2):
    count=0
    if t==0:
        # 첫번째를 이미 누른 후   110 - 001 
        tmp=a1
        count+=1
        tmp[0]=1-tmp[0]
        tmp[1]=1-tmp[1]
        # print("누름 ",tmp)
    else:
        tmp=a2 # 첫번째 안누를때
        # print("안누름 ",tmp)
    # 1,2,3,...,n-3,n-2,n-1
    for i in range(1,n):
        if tmp[i-1]==b[i-1]:
            continue
        else:
            count+=1
            for j in range(i-1,i+2):
                if j<n:
                    tmp[j]=1-tmp[j]
    # print("after ",tmp)
    for j in range(n):
        if tmp[j]!=b[j]:
            count=-1
            break
    if count!=-1:
        ans.append(count)

if ans:
    print(min(ans))
else:
    print("-1")

 


