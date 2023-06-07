"""
자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 자연수 n (1 ≤ n ≤ 1012)이 주어진다.
"""
import math
n=int(input())
res=n

for p in range(2, int(math.sqrt(n))+1): # 제곱근까지만 진행
    if n%p==0: # 소인수인지
        res-=res/p
        while n%p==0:
            n/=p

if n>1:   # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    res-=res/n

print(int(res))