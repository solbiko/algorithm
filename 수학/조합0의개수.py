"""
(n)의 끝자리  0의 개수를 출력하는 프로그램을 작성하시오.
 m
 n,m<=2,000,000,000
"""
n,m=map(int,input().split())

def count(x, k):
    cnt = 0
    while x:
        x//=k
        cnt+=x
    return cnt

print(min(count(n,5)-count(m,5)-count(n-m,5), count(n,2)-count(m,2)-count(n-m, 2)))

