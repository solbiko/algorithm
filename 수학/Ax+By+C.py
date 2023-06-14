"""
A, B, C가 주어졌을 때, Ax+By=C를 만족하는 (x, y)중에서 다음을 만족하는 것을 아무거나 찾아보자.
x, y는 정수
-1,000,000,000 ≤ x, y ≤ 1,000,000,000
"""
import math
a,b,c=map(int,input().split())

def execute(a,b):
    ret=[0]*2
    if b==0:
        ret[0]=1
        ret[1]=0
        return ret
    q=a//b  # 몫
    v=execute(b,a%b)   # 재귀형태로 유클리드 호제법 수행
    # 역순으로 올라오면서 x,y 계산
    ret[0]=v[1]
    ret[1]=v[0]-v[1]*q
    return ret


mgcd=math.gcd(a,b)

if c%mgcd!=0:
    print(-1)
else:
    mok=int(c/mgcd)
    ret=execute(a,b)
    print(ret[0]*mok, end=' ')
    print(ret[1]*mok)


