"""
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)
둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.
7 3
1231234
"""
n,k=map(int,input().split())
arr=list(map(int,input()))

stack=[]
for x in arr:
    while stack and k>0 and stack[-1]<x:
        stack.pop()
        k-=1
    stack.append(x)

if k!=0:
    stack=stack[:-k]

print(''.join(map(str,stack)))

