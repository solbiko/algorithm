"""
12015
1 ≤ N ≤ 1,000,000
1초

12738
1 ≤ N ≤ 1,000,000
-1,000,000,000 ≤ Ai ≤ 1,000,000,000
3초
"""
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

d=[]

# for i in arr:
#     if d[-1]<i:
#         d.append(i)
#     else:
#         left = 0
#         right = len(d)
#
#         while left<right:
#             mid = (right+left)//2
#             if d[mid]<i:
#                 left = mid+1
#             else:
#                 right = mid
#         d[right] = i
#

from bisect import bisect_left


for i in arr:
    k = bisect_left(d, i)
    if len(d) == k:
        d += [i]
    else:
        d[k] = i


print(len(d))