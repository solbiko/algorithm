"""
강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수

입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)
"""
import sys
input=sys.stdin.readline

d=[[0 for j in range(31)] for i in range(31)]

for i in range(0,31):
    d[i][1] = i  # i개 중에 1개를 뽑는 경우의 수 i
    d[i][0] = 1  # i개 중 1개도 선택하지 않는 경우의 수 1
    d[i][i] = 1  # i개 중에 i개를 선택하는 경우의 수 1개

for i in range(2,31):
    for j in range(1,i):
        d[i][j]=d[i-1][j]+d[i-1][j-1] # 조합 점화식

t=int(input())
for _ in range(0,t):
    n,m=map(int,input().split())
    print(d[m][n])