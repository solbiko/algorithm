"""
소수 7331 : 733, 73, 7 소수 (왼쪽부터 1,2,3,4 자리 모두 소수)
n(1~8)자리 숫자 중 신기한 소수 찾기
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())

# 소수판별
def isPrime(num): # 단순소수판별 함수 사용해도 시간안에 가능
    for i in range(2, int(num/2+1)):
        if num%i==0:
            return False
    return True


def dfs(x):
    if len(str(x))==n:
        print(x)
    else:
        for i in range(1,10): # 뒷자리 수 탐색
            if i%2==0: # 짝수인 경우 탐색 불필요
                continue
            # 1,3,5,7,9
            if isPrime(x*10+i): # 소수인경우
                dfs(x*10+i)

# 일의 자리 소수는 2,3,5,7이므로 4가지 수에서만 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)



