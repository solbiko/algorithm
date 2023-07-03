def solution(genres, plays):
    answer = []

    dic = {}
    dicsum = {}
    for i,(g,p) in enumerate(zip(genres, plays)):

        if g in dic:
            dic[g].append((p, i))
        else:
            dic[g] = [(p, i)]

        if g in dicsum:
            dicsum[g] += p
        else:
            dicsum[g]= p

    dicsum = sorted(dicsum.items(), key=lambda x: x[1], reverse=True)

    for (k, v) in dicsum:
        for (p,i) in sorted(dic[k], key=lambda x: (-x[0], x[1]))[:2]:
            print(p,i)
            answer.append(i)
        print()

    return answer