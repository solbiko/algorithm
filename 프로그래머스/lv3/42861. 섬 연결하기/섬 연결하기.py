def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    
    arr = [i for i in range(n)]
    def find(a):
        if a == arr[a]:
            return a
        else:
            arr[a] = find(arr[a])
            return arr[a]
   
    useEdge = 0
    for cost, s, e in edges:
        if find(s) != find(e):
            answer+=cost
            arr[find(s)]=e
            useEdge += 1
        
        if useEdge == n-1:
            break
            
    return answer