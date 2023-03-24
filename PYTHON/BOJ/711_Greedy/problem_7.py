# 12904번  A 와 B

# S 를 T 로 바꾸는 게임

s = list(input())
t = list(input())

# 문자열 뒤에 A 추가
# 문자열 뒤집고 뒤에 B 추가


while len(s)!=len(t):
    tmp = t.pop()
    if tmp=='A':
        continue
    if tmp=='B':
        t.reverse()
if "".join(s)=="".join(t):
    print(1)
else:
    print(0)


