# 2138번 전구와 스위치
n = int(input())
a=list(map(int,input()))
b=list(map(int,input()))

def tap(swit,idx):
    swit[idx]=1-swit[idx]
# 누른 표시를 함
count=0
    # print("check ",check)
for i in range(n):

    if i==0:
        if a[i]!=b[i]:
            tap(a,i)
            tap(a,i+1)
            count+=1   
            
    elif i==n-1:
        if a[i-1]!=b[i-1]:
            tap(a,i-1)
            tap(a,i)
            count+=1   

    elif 1<=i<=n-2:
        if a[i-1]!=b[i-1]:
            tap(a,i-1)
            tap(a,i)
            tap(a,i+1)  
            count+=1       
        
print(count)            


