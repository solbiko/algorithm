import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

n,m=map(int,input().split()) # 사람수, 친구관계수

list = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    list[s].append(e)
    list[e].append(s)

visitList = [False]*(n+1)
flag=0 # 도착확인 변수

def dfs(v, c): # 현재노드, 깊이
    global flag
    if c==5: # 깊이가 5인경우
        flag=1
        return
    visitList[v]=True
    for i in list[v]:
        # 현재 노드와 연결된 노드 중 방문하지 않은 노드로 DFS 실행
        if not visitList[i]:
            dfs(i, c+1) # 호출마다 깊이 증가
    visitList[v]=False

# 노드마다 DFS 실행
for i in range(n):
    dfs(i,1)
    if flag==1: # depth가 5에 도달한 적이 있다면 종료
        break

print(flag)
