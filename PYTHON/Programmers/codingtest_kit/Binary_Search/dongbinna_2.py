from bisect import bisect_left
from bisect import bisect_right
n,m = map(int,input().split()) # m인 원소의 개수
array = list(map(int,input().split()))

a=bisect_left(array,m)
b=bisect_right(array,m)

print(b-a)

