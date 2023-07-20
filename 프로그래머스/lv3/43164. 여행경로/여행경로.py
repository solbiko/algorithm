def solution(tickets):
    answer = []
    n=len(tickets)
    visited=[False]*len(tickets)
    
    def dfs(v, path):
        
        if len(path) == n+1:
            answer.append(path)
            return
        
        for i,ticket in enumerate(tickets):
            s,e=ticket
            if v==s and not visited[i]:
                visited[i] = True
                dfs(e, path+[e])
                visited[i] = False
        
    dfs("ICN",["ICN"])
    
    answer.sort()
    return answer[0]