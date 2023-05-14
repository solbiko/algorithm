"""
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.

준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
4 7
6 13
4 8
3 6
5 12
"""
import sys
input=sys.stdin.readline

# 물품수, 버틸무게
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

arr = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

for i in range(1, n+1):   # 물건 하나씩
    for j in range(1, k+1):  # 1~k무게까지 표 작성
        w = arr[i][0]
        v = arr[i][1]
        if j < w:   # 해당 물건이 더 큰 경우
            dp[i][j] = dp[i-1][j] # 이전가치를  그대로 사용
        else:   # 해당 물건이 들어가는 크기인 경우
            #이전 최대가치를 사용하는 것보다 이전걸 빼고 현재물건을 넣는게 더 좋다면 넣어줌
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

print(dp[n][k])