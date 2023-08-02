from queue import PriorityQueue

def solution(n, costs):
    answer = 0

    q = PriorityQueue()

    # 유니온파인드
    arr = [0]*n # 인덱스 리스트
    for i in range(n):
        arr[i]=i
    
    for s,e,cost in costs: # 에지 리스트
        q.put((cost,s,e))
        q.put((cost,e,s))

    def find(a):  # 대표노드 찾기
        if a == arr[a]:
            return a
        else:
            arr[a] = find(arr[a])
            return arr[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            arr[b] = a

    useEdge = 0
    while useEdge<n-1:
        w,s,e=q.get()
        if find(s) != find(e):
            union(s, e)
            answer+=w
            useEdge+=1

    return answer