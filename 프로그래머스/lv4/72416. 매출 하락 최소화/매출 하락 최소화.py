"""
워크숍에 참석할 직원들을 선발

모든 팀은 최소 1명 이상의 직원을 워크숍에 참석
워크숍에 참석하는 직원들의 하루평균 매출액의 합이 최소
10번 직원은 C팀과 D팀 모두에 속해 있으므로, 두 팀에서 모두 참석한 것으로 인정

참석하는 직원들의 하루평균 매출액의 합을 최소로 하려고 합니다. 그렇게 최소화된 매출액의 합
"""
INF = float('inf')
def solution(sales, links):
    
    s=[0]+sales
    n=len(s)

    d = [[0]*2 for i in range(n)] # d[node][0] 참석,  d[node][1] 불참

    def dfs(x):
        if not g[x]:
            d[x][0],d[x][1] = s[x],0
            return

        mingap = INF # 모든 팀이 워크샵에 참석해야 하는 조건을 만족시키기 위해 필요한 값
        d[x][0] = s[x] # x 참석 == x 매출 빠짐
         
        for i in g[x]:
            dfs(i)
            d[x][0] += min(d[i])
            mingap = min(mingap, d[i][0]-d[i][1]) # (참석 가중치 - 불참 가중치) 가장 작은 노드를 선택
            
        if mingap < 0: 
            mingap = 0
        d[x][1] = d[x][0]+mingap-s[x] # x 불참 =  각 자식노드들 참여/불참 경우 최소 가중치 중 작은 값들만을 더하기

    
    g = [[] for i in range(n)]
    for x in links:
        g[x[0]].append(x[1])
        
    dfs(1)
    return min(d[1])