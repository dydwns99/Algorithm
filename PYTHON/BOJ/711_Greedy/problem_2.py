# 1744번  수 묶기

# 수열에서 두 수의 묶음들을 곱해 합의 최댓값 구하기

# 입력
n = int(input())
plu=[]
miu=[]
etc=[]
for _ in range(n):
    num = int(input())
    if num>1:
        plu.append(num)
    elif num<=0:
        miu.append(num)
    else:
        etc.append(num)
plu.sort(reverse=True)
miu.sort()
# print("plu : ",plu)
# print("miu : ",miu)
# 양수에선 짝수면 두개씩 곱해서 더하고
sum=0
if len(plu)%2==0 and plu:

    for i in range(0,len(plu),2):
        tmp=plu[i]*plu[i+1]
        sum+=tmp
elif len(plu)%2!=0 and plu:   # 2 3 5
    sum+=plu[len(plu)-1]
    # 홀수면 2번째 원소부터 두개씩 곱해서 더함
    for i in range(0,len(plu)-1,2):
        tmp=plu[i]*plu[i+1]
        sum+=tmp
# print("af plu : ",sum)
# 음수에서도
if len(miu)%2==0 and miu:
    for i in range(0,len(miu),2):
        tmp=miu[i]*miu[i+1]
        sum+=tmp
elif len(miu)%2!=0 and miu:
    sum+=miu[len(miu)-1]
    for i in range(0,len(miu)-1,2):
        tmp=miu[i]*miu[i+1]
        sum+=tmp
# print("af miu : ", sum)
for i in range(len(etc)):
    sum+=etc[i]
print(sum)