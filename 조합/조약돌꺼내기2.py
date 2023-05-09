"""
조약돌이 N개. 조약돌의 색상은 1부터 M까지 중의 하나
조약돌을 랜덤하게 K개 뽑았을 때, 뽑은 조약돌이 모두 같은 색일 확률

색깔 수 M (1 ≤ M ≤ 50)
각 색상의 조약돌 개수(1~50)
뽑을 개수 K(1 ≤ K ≤ N)
3
5 6 7
2

2. 한 색깔의 조약돌만 뽑을 확률을 색깔별로 모두 구하고 각각의 확률을 더함
"""

import sys
input=sys.stdin.readline


m = int(input()) # 색 종류개수
arr = list(map(int,input().split())) # 색깔별 조약돌 개수
t = sum(arr) # 전체 조약돌 개수
p= [0]*51 # 색깔별 확률 저장 리스트


k = int(sys.stdin.readline()) # 뽑을 개수
ans=0

for i in range(0,m): # 조약돌 색깔별로
    # 뽑을 개수보다 같은색 조약돌의 개수가 적은 경우 : 모두 같은 색으로 뽑을 확률 0
    if k <= arr[i] :
        # k번 뽑을 동안 같은 색이 나올 확률 : 5/18 * 4/17
        p[i]=1 # 확률 초기값
        for j in range(0,k):
            # i색깔을 모두 뽑을 확률 * 현재 색깔 개수-k / 전체 조약돌 개수-k
            p[i]=p[i]*(arr[i]-j)/(t-j)
        ans+=p[i]

print(ans)