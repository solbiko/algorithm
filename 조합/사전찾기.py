"""
특별한 문자열로 이뤄진 사전 만들기
사전에 수록돼 있는 문자열은 N(1~100)개의 a, M개의 z
알파벳 순서대로 수록

k(1,000,000,000)번째 문자열 출력
"""
import sys
input = sys.stdin.readline

n,m,k=map(int,input().split())

d = [[0 for i in range(202)] for j in range(202)]

# 조합 테이블 생성
for i in range(0,201):
    for j in range(0,i+1):
        if i==0 or i==j:
            d[i][j]=1
        else:
            # 조합 점화식
            d[i][j] = d[i-1][j]+d[i-1][j-1]
            if d[i][j] > 1000000000:
                d[i][j] = 10000000001 # k범위가 넘어가면 범위의 최댓값 저장

if d[n+m][m] < k: # 주어진 자릿수로 만들 수 없는 k번째 수의 경우
    print(-1)
else: # 문자 선택
    while not (n==0 and m==0): # 모든 문자를 사용할 때까지

        #d[n-1+m][m] : a문자를 선택했을 때 남은 문자열들로 만들 수 있는 모든 경우의 수
        if d[n-1+m][m] >= k: # a를 선택해도 남은 경우의 수가 k보다 큰 경우
            print("a", end='')
            n-=1
        else:
            print("z", end='')
            k-=d[n-1+m][m] # k의 값을 계산된 모든 경우의 수를 뺀 값으로 저장
            m-=1




