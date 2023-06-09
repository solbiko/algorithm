"""
2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 좌표값은 절댓값이 100,000을 넘지 않는 정수이다.
"""
import sys
input=sys.stdin.readline
n=int(input())
x=[]
y=[]

for i in range(n):
    tmpX,tmpY=map(int,input().split())
    x.append(tmpX)
    y.append(tmpY)

# 리스트에 마지막에 처음 점 다시 넣기 -> 마지막 점과 처음 점도 CCW 포함
x.append(x[0])
y.append(y[0])

res=0
for i in range(n):
    res+=(x[i]*y[i+1])-(x[i+1]*y[i])

print(round(abs(res/2),1))