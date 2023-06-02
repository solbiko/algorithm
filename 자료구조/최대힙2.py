import sys
input=sys.stdin.readline
from heapq import heappush, heappop

n=int(input())
q = []

for _ in range(n):
    num=int(input())
    if num==0:
        if len(q) > 0:
            print(heappop(q)[1])
        else:
            print(0)
    else:
        heappush(q, (-num, num))