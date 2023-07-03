from string import ascii_uppercase
def solution(msg):
    answer = []

    c = [i for i in range(1, 27)]
    a = dict(zip(ascii_uppercase, c))

    w = ''
    for x in msg:
        w += x
        if w not in a:
            a[w] = len(a) + 1
            answer.append(a[w[:-1]])
            w = w[-1]

    answer.append(a[w])
    return answer