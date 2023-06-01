"""
중위 표기식을 후위 표기식으로 변환
우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다. 그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다.
그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다.
마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.
표기식은 알파벳 대문자와 +, -, *, /, (, )

A*(B+C) ABC+*
A+B*C ABC*+
A+B*C-D/E ABC*+DE/-
"""
arr=list(input())
res=''
stack=[]
for x in arr:
    if x.isalpha():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'): # 연산자 우선순위가 같을 때
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and  stack[-1]!='(': # 괄호 안의 연산자가 아닐 때
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(': # 여는 괄호까지 연산자 pop
                res += stack.pop()
            stack.pop() # ( 없애기

# 스택에 남아있는 것
while stack:
    res+=stack.pop()

print(res)
