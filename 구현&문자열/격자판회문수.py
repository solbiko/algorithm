"""
1부터 9까지의 자연수로 채워진 7*7 격자
격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 출력

2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
"""
import sys
input=sys.stdin.readline

a=[list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(7):
    for j in range(3):
        tmp=a[i][j:j+5]

        # 행 회문검사
        if tmp==tmp[::-1]:
            cnt+=1

        # 열 회문검사
        for k in range(2):
            if a[j+k][i]!=a[j+5-k-1][i]:
                break
        else:
            cnt+=1

print(cnt)