"""
현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습 니다.
다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자 만 뽑기로 했습니다.
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.

지원자의 수 N(5<=N<=50)
N명의 키와 몸무게 정보가 차례로 주어집니다. 각 선수의 키와 몸무게는 모두 다릅니다.

첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력
5
172 67
183 65
180 70
170 72
181 60
"""
import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    h,w=map(int,input().split())
    a.append((h,w))

a.sort(reverse=True)

cnt=0
max=0
for h,w in a:
    if w>max:
        max=w
        cnt+=1

print(cnt)