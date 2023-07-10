def solution(s):
    stack=[]
    
    for x in s:
        if stack:
            if stack[-1]!=x:
                stack.append(x)
            else:
                stack.pop()
        else:
            stack.append(x)
                
    return 1 if len(stack)==0 else 0