"""
집합 Zn을 0부터 n-1까지의 정수 집합이라고 하자.
Zn ∋ a, b, c 일 때,
(a+b) mod n = 0이면 b는 a의 덧셈역이라고 하고
(a*c) mod n = 1이면 c는 a의 곱셈역이라고 한다.
정수 N, A가 주어졌을 때 Zn에서의 A의 덧셈역과 곱셈역을 구하시오.
단, 곱셈역을 구할 수 없으면 -1을 출력한다.
"""

N, A = map(int, input().split())

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


if gcd(A, N) != 1:
    inv = -1
else:
    inv = xgcd(A, N)
    while inv <= 0:
        inv += N

print(N-A, inv)