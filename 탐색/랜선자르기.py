"""
K개의 랜선은 길이가 제각각이다.
선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm은 버려야 한다.
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
이때 만들 수 있는 최대 랜선의 길이 출력

이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
이미 가지고 있는 각 랜선의 길이

첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이 출력

4 11
802
743
457
539

200

802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.
"""
import sys
input=sys.stdin.readline

k,n=map(int,input().split())
a=[]
for _ in range(k):
    a.append(int(input()))

def count(len): # 길이로 만들 수 있는 랜선갯수
    cnt=0
    for x in a:
        cnt+=(x//len)
    return cnt

# 이분탐색
l=1
r=max(a)
while l<=r:
    mid=(l+r)//2
    if count(mid)>=n:
        res=mid
        l=mid+1
    else:
        r=mid-1
print(res)