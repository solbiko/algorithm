"""
2 ≤ info의 길이 ≤ 17
당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다.
당신은 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.
"""


def solution(info, edges):
    answer = []

    n = len(info)  # 노드수

    def dfs(scnt, wcnt):  # 양수, 늑대수
        if scnt > wcnt:
            answer.append(scnt)
        else:
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1

                if info[child] == 0:  # 양
                    dfs(scnt + 1, wcnt)
                else:  # 늑대
                    dfs(scnt, wcnt + 1)
                visited[child] = 0

    n = len(info)  # 노드수
    visited = [0] * n
    visited[0] = 1
    dfs(1, 0)

    return max(answer)

    return answer