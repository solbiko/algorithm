"""
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하 여 가장 큰 수를 만들라고 했습니다. 단 숫자의 순서는 유지해야 합니다
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.
5276823 3
"""
n,m=map(int, input().split())
n=list(map(int, str(n)))
stack=[]
for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:-m]
print(''.join(map(str,stack)))