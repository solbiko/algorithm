def solution(n, computers):
    answer = 0
    visited=[False]*n

    
    def BFS(v):
        queue=[]
        visited[v]=True
        queue.append(v)

        while queue:
            now=queue.pop(0)
            visited[now]=True

            for i in range(n):
                if i!=now and not visited[i] and computers[now][i]==1:
                    queue.append(i)

    for x in range(n):
        if not visited[x]:
            BFS(x)
            answer+=1
            
    return answer