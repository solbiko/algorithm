"""
임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 출력

자연수 N(3<=N<=1,000,000), M
N개의 수
8 32
23 87 65 12 57 32 99 81
"""
import sys
sys.setrecursionlimit(10000)
from bisect import bisect_left


n,m=map(int,input().split())
a=list(map(int, input().split()))
a.sort()

# print(bisect_left(a, m)+1)


l=0
r=n-1

while l<=r:
    mid=(l+r)//2
    if a[mid]==m:
        print(mid+1)
        break

    if a[mid]>m:
        r=mid-1
    else:
        l=mid+1
