def solution(elements):
    n = len(elements)
    
    elements = elements*2
    s = set()
    for i in range(n):
        for j in range(i,n+i):
            s.add(sum(elements[i:j]))
            
    return len(s)