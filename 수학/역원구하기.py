"""
집합 Zn을 0부터 n-1까지의 정수 집합이라고 하자.
Zn ∋ a, b, c 일 때,
(a+b) mod n = 0이면 b는 a의 덧셈역이라고 하고
(a*c) mod n = 1이면 c는 a의 곱셈역이라고 한다.

정수 N, A가 주어졌을 때 Zn에서의 A의 덧셈역과 곱셈역을 구하시오.
단, 곱셈역을 구할 수 없으면 -1을 출력한다.
"""

n,a= map(int, input().split())

addInv=n-a  # 덧셈역원
mulInv=-1  # 곱셈역원

def gcd(a, b):
    return gcd(b, a%b) if b else a

def xgcd(a, b):
    r1=a
    r2=b
    s1=t2=1
    s2=t1=0

    while True:
        q=r1//r2  # 몫
        r=r1-(q*r2)
        s = s1-(q*s2)
        t = t1-(q*t2)
        if r == 0:
            return s2

        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

if gcd(a,n)!=1:  #  곱셈역을 구할 수 없는 경우 -1을 출력, a*s 와 n이 서로소가 아니라는 것
    print(addInv, mulInv)
else:
    # xgcd(11*x,26)=1이 되는 x를 찾는 것 -> 11*s+26*t=1일 때 s값(곱셈역)
    mulInv=xgcd(a,n)
    while mulInv<=0:  # s가 양수인 경우
        mulInv+=n

print(addInv, mulInv)