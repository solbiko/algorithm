"""
3 7 5 2 6 1 4
아이들을 순서대로 줄을 세우기 위해, 먼저 4번 아이를 7번 아이의 뒤로 옮겨보자. 그러면 다음과 같은 순서가 된다.
3 7 4 5 2 6 1
이제, 7번 아이를 맨 뒤로 옮긴다.
3 4 5 2 6 1 7
다음 1번 아이를 맨 앞으로 옮긴다.
1 3 4 5 2 6 7
마지막으로 2번 아이를 1번 아이의 뒤로 옮기면 번호 순서대로 배치된다.
1 2 3 4 5 6 7

N명의 아이들이 임의의 순서로 줄을 서 있을 때, 번호 순서대로 배치하기 위해 옮겨지는 아이의 최소 수를 구하는 프로그램을 작성하시오
첫째 줄에는 아이들의 수 N이 주어진다. 둘째 줄부터는 1부터 N까지의 숫자가 한 줄에 하나씩 주어진다.
N은 2 이상 200 이하의 정수이다.
7
3
7
5
2
6
1
4
"""
import sys
input=sys.stdin.readline

n = int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(n - max(dp))