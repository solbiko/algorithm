def solution(id_list, report, k):
    answer = [0] * len(id_list)
    r = {x: 0 for x in id_list}

    for x in set(report):
        r[x.split()[1]] += 1

    for x in set(report):
        s, e = x.split()
        if r[e] >= k:
            answer[id_list.index(s)] += 1

    return answer