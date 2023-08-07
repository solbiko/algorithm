def solution(a):
    stack = []

    for x in a:
        if len(stack) < 2:
            stack.append(x)
        else:
            while(len(stack) >= 2 and stack[-2] < stack[-1] > x):
                stack.pop(-1)
            stack.append(x)

    return len(stack)