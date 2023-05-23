"""
완성된 9×9 크기의 스도쿠가 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출력
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
"""
import sys
input=sys.stdin.readline

def check(a):

    for i in range(9):
        ch1 = [0] * 10 # 행 체크
        ch2 = [0] * 10 # 열 체크
        for j in range(9): # 1-9까지 숫자가 있는 경우 방문 처리
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1)!=9 and sum(ch2)!=9:
            return False

    # 3*3 그룹
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10 # 3*3 체크
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True

# 격자판
a=[list(map(int,input().split())) for _ in range(9)]
print("YES" if check(a) else "NO")


