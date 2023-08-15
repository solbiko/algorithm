import sys
sys.setrecursionlimit(10**6)

l = [0] * 10000
r = [0] * 10000
x = [0] * 10000
parent = [-1] * 10000
cnt = root = 0


def solution(k, num, links):
    global root
    
    def DFS(curr, limit):
        global cnt
        left = right = 0
        if l[curr] != -1: left = DFS(l[curr], limit)
        if r[curr] != -1: right = DFS(r[curr], limit)

        # CASE 1: 모두 포함되는 경우
        if x[curr] + left + right <= limit:
            return x[curr] + left + right

        # CASE 2: limit보다 커서 한쪽 그룹을 자르는 경우
        if x[curr] + min(left, right) <= limit:
            cnt += 1
            return x[curr] + min(left, right)

        # CASE 3: limit보다 커서 두쪽 그룹을 자르는 경우
        cnt += 2
        return x[curr]

    def solve(limit):
        global cnt
        cnt = 0
        DFS(root, limit)
        cnt += 1
        return cnt


    n = len(num)

    for i in range(len(links)):
        x[i] = num[i]
        l[i], r[i] = links[i]
        if l[i] != -1: parent[l[i]] = i
        if r[i] != -1: parent[r[i]] = i

    for i in range(n):
        if parent[i] == -1:
            root = i; break

    start = max(x)
    end = sum(x)
    while start < end:
        mid = (start + end) // 2
        if solve(mid) <= k:
            end = mid
        else: start = mid + 1
        
    return start
