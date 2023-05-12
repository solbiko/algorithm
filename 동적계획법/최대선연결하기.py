"""
왼쪽의 번호와 오른쪽의 번호, 같은 번호끼리 선으로 연결
왼쪽번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순으로 나열
오른쪽의 번호 정보가 위부터 아래 순서
서로 선이 겹치지 않고 최대 몇 개의 선 연결?

자연수 N(1<=N<=100)
1부터 N까지의 자연수 N개의 오른쪽 번호 정보

10
4 1 2 3 9 7 5 6 10 8
=> 6개 (123568)
"""
from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d=[]

for i in arr:
    k = bisect_left(d, i)
    if len(d) == k:
        d += [i]
    else:
        d[k] = i

# print(d)
print(len(d))