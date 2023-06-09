"""
2차원 좌표 평면 위에 있는 점 3개 P1, P2, P3가 주어진다. P1, P2, P3를 순서대로 이은 선분이 어떤 방향을 이루고 있는지 구하는 프로그램을 작성하시오.
첫째 줄에 P1의 (x1, y1),
둘째 줄에 P2의 (x2, y2),
셋째 줄에 P3의 (x3, y3)가 주어진다.
(-10,000 ≤ x1, y1, x2, y2, x3, y3 ≤ 10,000) 모든 좌표는 정수이다.
P1, P2, P3의 좌표는 서로 다르다.
"""
import sys
input=sys.stdin.readline

x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
x3,y3=map(int, input().split())

# CCW 공식
result=(x1*y2 + x2*y3 + x3*y1)-(x2*y1 + x3*y2 + x1*y3)

if result>0:  # 반시계
    print(1)
elif result<0:  # 시계
    print(-1)
else:  # 일직선
    print(0)