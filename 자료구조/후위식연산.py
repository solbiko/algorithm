"""
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
"""
arr=list(input())
res=''
stack=[]
for x in arr:
    if x.isdecimal():
        stack.append(x)
    else:
        a=int(stack.pop())
        b=int(stack.pop())
        if x=='+':
            stack.append(b+a)
        if x == '-':
            stack.append(b-a)
        if x == '/':
            stack.append(b/a)
        if x == '*':
            stack.append(b*a)

print(int(stack[0]))