"""
정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.

10장, 20장, 40장의 묶음
10+20, 40 => 30, 40 : (10 + 20) + (30 + 40) = 100번의 비교
10+40, 20 => 50, 20 : (10 + 40) + (50 + 20) = 120번의 비교

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 출력
3
10
20
40
"""
import sys
input=sys.stdin.readline
from queue import PriorityQueue

q = PriorityQueue()

n=int(input())
for _ in range(n):
    q.put(int(input()))

cnt=0
while q.qsize() > 1:
    sum= q.get()+q.get()
    cnt+=sum
    q.put(sum)

print(cnt)