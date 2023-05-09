"""
조약돌이 N개. 조약돌의 색상은 1부터 M까지 중의 하나
조약돌을 랜덤하게 K개 뽑았을 때, 뽑은 조약돌이 모두 같은 색일 확률

첫째 줄에 M (1 ≤ M ≤ 50)
둘째 줄에는 각 색상의 조약돌이 몇 개 있는지 주어진다.
각 색상의 조약돌 개수(1~50)
셋째 줄에는 K(1 ≤ K ≤ N)

1. 색깔별 조약돌의 개수에서 k를 뽑을 수 잇는 경우의수 / 전체 돌에 관해 k개를 뽑는 경우의 수
"""
import sys
input=sys.stdin.readline

import math

m = int(input()) # 색 종류개수
arr = list(map(int,input().split())) # 색깔별 조약돌 개수
k = int(sys.stdin.readline()) # 뽑을 개수

t = sum(arr) # 전체 조약돌 개수
total = math.comb(t, k) # 전체 돌에 관해 k개를 뽑는 경우의 수

same_color = 0 # 색깔별 조약돌의 개수에서 k를 뽑을 수 잇는 경우의 수
for s in arr:
    same_color += math.comb(s, k)

print(same_color/total)