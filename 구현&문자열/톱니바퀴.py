""""
톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다


1~4 톱니바퀴 상태
12시방향부터 시계방향 순서(N극 0, S극 1)

회전 횟수 K(1 ≤ K ≤ 100)
톱니바퀴의 번호, 방향(1 시계, -1 반시계)

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
"""
import sys
from collections import deque
input=sys.stdin.readline

t=[deque(input().strip()) for _ in range(4)]  # 톱니바퀴

k=int(input())  # 회전횟수
l = []  # 회전정보

for _ in range(k):
    tIdx, direction=map(int, input().split())
    center = tIdx-1
    center2 = t[center][2]
    center6 = t[center][6]

    x=direction
    for i in range(center-1, -1, -1): # 이전 톱니바퀴를
        if t[i][2] != center6:  # 이후 톱니바퀴랑 비교
            center6 = t[i][6]
            t[i].rotate(-1*x)
            x*=-1  # 방향 번갈아
        else:
            break

    x=direction
    for i in range(center+1, 4): # 이후 톱니바퀴를
        if t[i][6] != center2:  # 이전 톱니바퀴와 비교
            center2 = t[i][2]
            t[i].rotate(-1*x)
            x*=-1  # 방향 번갈아
        else:
            break

    t[center].rotate(direction)

sum=0
for i in range(4):  # 1248
    if t[i][0]=='1':
        sum+=2**i
print(sum)

