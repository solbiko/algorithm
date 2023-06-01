"""
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
5
ABC*+DE/-
1
2
3
4
5
"""
n=int(input())
arr=input()

nList=[] # 피연산자
for _ in range(n):
    nList.append(int(input()))

stack=[]
for x in arr:
    if x.isalpha():
        num=nList[ord(x)-ord('A')]
        stack.append(num)
    else:
        a=stack.pop()
        b=stack.pop()
        if x=='+':
            stack.append(b+a)
        if x == '-':
            stack.append(b-a)
        if x == '/':
            stack.append(b/a)
        if x == '*':
            stack.append(b*a)

print('%.2f' %stack[0])