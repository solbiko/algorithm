"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
"""
import sys
input=sys.stdin.readline

n=int(input())
count=[0]*10001  # 카운팅 정렬 리스트

for i in range(n):
    count[int(input())]+=1

for i in range(10001):
    if count[i]!=0:
        for _ in range(count[i]):
            print(i)
print(count)