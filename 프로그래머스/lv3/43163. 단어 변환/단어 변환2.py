from collections import deque
def solution(begin, target, words):
    dist = {begin: 0}
    def search(now): # 현재 단어
        for word in words:
            if len(now) != len(word):
                continue

            count = 0
            for c, w in zip(now, word):
                if c != w:
                    count += 1

            if count == 1:
                yield word


    q = deque([begin])
    while q:
        word = q.popleft()

        for new_word in search(word):
            if new_word not in dist:
                dist[new_word] = dist[word] + 1
                q.append(new_word)

    return dist.get(target, 0)

print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))