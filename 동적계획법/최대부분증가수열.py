"""
N(2≤N≤1,000, 자연수)
8
5 3 7 8 6 2 9 4
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)

d=[0]*(n+1)
d[1]=1

res=0

for i in range(2,n+1):
    max=0
    # print("i ", i, "arr[i] ", arr[i])
    for j in range(i-1, 0, -1):
        # print("j ", j, "arr[j] ", arr[j])
        if arr[j]<arr[i] and d[j]>max:
            max=d[j]
    d[i]=max+1
    if d[i]>res:
        res=d[i]

print(res)

