def r(w):
    a=0
    for i in range(len(w)):
        if w[i] == "(":
            a+=1
        else:
            a-=1
        if a==0:  # 균형잡힌
            return w[:i+1], w[i+1:]


def ck(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''

    # 1
    if not p:
        return ''

    # 2
    u, v = r(p)

    if ck(u):  # 3
        return u + solution(v)  # 3-1
    else:  # 4
        answer += '('  # 4-1
        answer += solution(v)  # 4-2
        answer += ')'  # 4-3

        for j in u[1:len(u) - 1]:  # 4-4
            if j == '(':
                answer += ')'
            else:
                answer += '('
        # 4-5
        return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
