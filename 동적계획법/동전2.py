"""
n가지 종류의 동전이 있다.
이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
다음 n개의 줄에는 각각의 동전의 가치(1~100,000 자연수)가 주어진다.

첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
3 15
1
5
12
"""
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
c = [int(input()) for i in range(n)]

d=[sys.maxsize]*(k+1) # dp[i]= i원을 거슬러 줄 동전의 최소개수
d[0]=0

for i in range(n):
    for j in range(c[i],k+1):
        d[j]=min(d[j], d[j-c[i]]+1)

if d[k] == sys.maxsize:
   print(-1)
else:
   print(d[k])
