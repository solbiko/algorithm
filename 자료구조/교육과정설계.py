"""
수업중에는 필수과목이 있습니다. 이 필수과목은 반드시 이수해야 하며, 그 순서도 정해져 있 습니다.
만약 총 과목이 A, B, C, D, E, F, G가 있고, 여기서 필수과목이 CBA로 주어지면 필수과목은 C, B, A과목이며 이 순서대로 꼭 수업계획을 짜야 합니다.
수업계획은 그 순서대로 앞에 수업이 이수되면 다음 수업을 시작하다는 것으로 해석합니다.
필수과목순서가 주어지면 현수가 짠 N개의 수업설계가 잘된 것이면 “YES", 잘못된 것이면 ”NO“를 출력

첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
두 번째 줄에 N(1<=N<=10)이 주어집니다.
세 번 째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다) 수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.

CBA
3
CBDAGE
FGCDAB
CTSBDEA

#1 YES
#2 NO
#3 YES
"""
from collections import deque
import sys
input=sys.stdin.readline

need=list(input())
n=int(input())

for i in range(n):
    plan=input()
    queue = deque(need)
    for x in plan:
        if x in queue:
            if x!=queue.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(queue)==0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))