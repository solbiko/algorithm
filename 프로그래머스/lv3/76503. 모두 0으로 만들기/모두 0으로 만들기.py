import sys
sys.setrecursionlimit(10**9)
answer=0

def solution(a, edges):
    
    if sum(a)!=0:
        return -1

    graph=[[] for _ in range(len(a))]
    for s,e in edges:
        graph[s].append(e)
        graph[e].append(s)
        
    def dfs(idx, pidx):
        global answer

        for i in graph[idx]:
            if i != pidx:
                dfs(i, idx)

        a[pidx] += a[idx]
        answer += abs(a[idx])
        a[idx] = 0

    dfs(0, 0)

    return answer