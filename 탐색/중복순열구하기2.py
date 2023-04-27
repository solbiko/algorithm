"""
1부터 N까지 번호가 적힌 구슬
이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력

N(3<=N<=10), M(2<=M<=N)
맨 마지막 총 경우의 수를 출력
"""
from itertools import product

import sys
input=sys.stdin.readline
n,m=map(int, input().split())

arr=[i+1 for i in range(n)]
combi = product(arr, repeat=m)

total=0
for i in combi:
    for j in i:
        print(j, end=" ")
    print()
    total+=1
print(total)