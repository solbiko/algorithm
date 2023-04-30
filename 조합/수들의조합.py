"""
N개의 정수
K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수 는 몇 개가 있는지 출력

5개의 숫자 2 4 5 8 12
3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면 4+8+12 2+4+12로 2가지

첫줄 정수개수 N(3<=N<=20), 임의의 정수 K(2<=K<=N)
두 번째 줄 N개의 정수
세 번째 줄 M

5 3
2 4 5 8 12
6
"""

import sys
input=sys.stdin.readline
import itertools as it

n,k=map(int,input().split())
arr=list(map(int, input().split()))
m=int(input())

cnt=0
for x in it.combinations(arr,k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)