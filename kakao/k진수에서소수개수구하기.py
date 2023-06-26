def solution(n, k):
    import math

    # k진수 변환
    word = ''
    while n:
        word = str(n % k) + word
        n = n // k

    arr = word.split("0")

    answer = 0
    for i in arr:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue

        flag = True
        for j in range(2, int(math.sqrt(int(i)) + 1)):
            if int(i) % j == 0:
                flag = False
                break
        if flag:
            answer += 1

    return answer

print(solution(437674,3))