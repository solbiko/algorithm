"""
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성
단 재귀함수를 이용 해서 출력
"""

n=int(input())

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')
DFS(n)


