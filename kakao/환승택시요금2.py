def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    graph = [[INF for j in range(n)] for i in range(n)]

    for f in fares:
        i, j, k = f
        graph[i-1][j-1]=k
        graph[j-1][i-1]=k

    print(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    print(graph)

    for i in range(n):
        temp = graph[s-1][i] + graph[i][a-1] + graph[i][b-1]
        answer = min(temp, answer)

    return answer



print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))