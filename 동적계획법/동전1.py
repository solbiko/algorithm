"""
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오.
각각의 동전은 몇 개라도 사용할 수 있다.
사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
다음 n개의 줄에는 각각의 동전의 가치(1~100,000 자연수)가 주어진다.

3 10
1
2
5
"""
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
c = [int(input()) for i in range(n)]

# dp[i] : j원을 만들 수 있는 경우의 수
dp = [0 for _ in range(k+1)]
dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1로 초기화

for i in range(n): # 각 동전마다
    for j in range(k+1): # k원까지
        if j-c[i] >= 0:
            dp[j] += dp[j-c[i]]
print(dp[k])