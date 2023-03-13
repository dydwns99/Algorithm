# 1285번 동전 뒤집기
from collections import Counter
import copy
# 뒷면이 위를 향하여 놓일 수 있는 동전의 최소 개수 출력

n = int(input())
coins=[]
for i in range(n):
    row = list(input())
    coins.append(row)
for c in coins:
    print(c)
print("---")
def change(array):
    for coin in array:
        counter = Counter(coin)
        if counter['T']>counter['H']:
            for i in range(len(coin)):
                if coin[i]=='T':
                    coin[i]='H'
                else:
                    coin[i]='T'
def revs(a,b):
    for i in range(n):
        for j in range(n):
            a[i][j]= b[j][i]
 
# 행 먼저 바꿈
coina=copy.deepcopy(coins)
change(coina)
# for c in coina:
#     print(c)
# print("---")

# 열 먼저 바꿈
coinb=[[0]*n for _ in range(n)]
revs(coinb,coins)
change(coinb)

# 그 후
new_a=[[0]*n for _ in range(n)] 
revs(new_a,coina)
change(new_a)
counta=0
for i in range(n):
    for j in range(n):
        if new_a[i][j]=="T":
            counta+=1
# print("counta : ",counta)

new_b=[[0]*n for _ in range(n)] 
revs(new_b,coinb)
change(new_b)
countb=0
for i in range(n):
    for j in range(n):
        if new_b[i][j]=="T":
            countb+=1
# print("countb : ",countb)
print(min(counta,countb))











