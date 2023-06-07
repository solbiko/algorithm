"""
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
"""
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

T=int(input())
for _ in range(T):
    A,B=map(int, input().split())
    print(int(A*B/gcd(A,B)))


# import math
# for _ in[0]*int(input()):
#     print(math.lcm(*map(int,input().split())))
