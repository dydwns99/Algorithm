# 12970번  AB

# n : 문자열 S의 길이  , k : (A,B) 쌍의 개수

n, k = map(int, input().split())

# 조건을 만족하는 문자열 S 출력

# 문자열을 만들 수 없는 경우?
# 0 0 0 0 0
# 맨 처음 발견된 A 를 기준으로 오른쪽에 있는 B의 개수를 확인
# 그 다음 발견된 A 를 기준으로 오른쪽에 있는 B의 개수 확인
# A의 개수에 따른 최댓값
# A B B B B B B B B B -> 9-> 최대 n-1 개
# A B B B B B B A B B -> 8 2 ->  최대 n-2+n-2 개
# A 2개일 때 8 + 0,1,2,3,4,5,6,7,8 -> 최대 n-3+n-3+n-3개
# A 3개일 때  7 + 7 + 0,1,2,3,4,5,6,7

idx=-1
for i in range(1,n+1):
  if k==0: # 쌍이 필요 없을 때  앞에
      idx=n
      break
  if k <= (n-i) * i:
#       문자열을 만듬 -> A의 개수가 i개 일때 이므로 개수를 빼냄
      idx=i
      break
# print(idx)

# 처음엔 A들을 왼쪽으로 밀착시킴
tmp=[]
for i in range(idx):
    tmp.append('A')
for i in range(n-idx):
    tmp.append('B')
# print(tmp)

# A A A A B B B
# 그 다음에 맨 오른쪽 A를 오른쪽으로 한칸씩 미룸
count = (n-idx) * idx
for j in range(idx-1, -1, -1):

    for i in range(j, n-1):
        if count==k or count<0:
          break
        tmp[i] = 'B'
        tmp[i+1] = 'A'
        count -= 1

    if count==k:
        break
# print(tmp)
# print("출력")
if idx==-1:
    print(idx)
else:
    if 'B' not in tmp:
        tmp[0]='B'
        print("".join(tmp))
    else:
        print("".join(tmp))
