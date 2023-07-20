def solution(number, k):
    stack = []

    for x in number:
        while stack and stack[-1]<x and k>0:
            k-=1
            stack.pop()
        stack.append(x)
        
    return ''.join(stack[:len(stack)-k])
