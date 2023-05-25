"""
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.

C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력

자연수 N(3<=N<=200,000)과 C(2<=C<=N)
마구간의 좌표 xi(0<=xi<=1,000,000,000)
5 3
1
2
8
4
9
"""
import sys
input=sys.stdin.readline

n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))

a.sort()
l=1
r=a[n-1]

def count(len): # 배치한 말 수 체크
    cnt=1
    ep=a[0] # 마지막으로 배치한 말의 좌표
    for i in range(1,n):
        if a[i]-ep >= len: # 두 말사이 거리 len을 두고 배치 가능하다면
            cnt+=1 # 마 수 증가
            ep=a[i] # 마지막 말 좌표 변경
    return cnt

# 이분탐색
while l<=r:
    mid=(l+r)//2
    if count(mid)>=c: # 배치해야 하는 말의수보다 배치한 말의 수가 크다면
        res=mid # 말 사이 거리
        l=mid+1 # 말 사이 거리 증가
    else: # 거리가 너무 길어서 배치해야하는 말을 다 배치하지 못하면
        r=mid-1 # 말 사이 거리 감소

print(res)


