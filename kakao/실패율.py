def solution(N, stages):
    answer = []

    a = [0] * (N + 1)
    for x in stages:
        a[x - 1] += 1

    b = {}
    for i in range(N):
        if sum(a[i:]) != 0:
            b[i + 1] = a[i] / sum(a[i:])
        else:
            b[i + 1] = 0

    b = sorted(b.items(), key=lambda x: x[1], reverse=True)

    for x in b:
        answer.append(x[0])

    return answer

print(solution(5	,[2, 1, 2, 6, 2, 4, 3, 3]))