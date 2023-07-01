from collections import Counter


def solution(str1, str2):
    answer = 0
    str1, str2 = str1.upper(), str2.upper()

    a = []
    for i in range(1, len(str1)):
        if str1[i - 1].isalpha() and str1[i].isalpha():
            a.append(str1[i - 1] + str1[i])

    b = []
    for i in range(1, len(str2)):
        if str2[i - 1].isalpha() and str2[i].isalpha():
            b.append(str2[i - 1] + str2[i])

    if len(a) == len(b) == 0:
        return 65536

    a = Counter(a)
    b = Counter(b)

    c = list((a & b).elements())
    u = list((a | b).elements())

    return int(len(c) / len(u) * 65536)

print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))