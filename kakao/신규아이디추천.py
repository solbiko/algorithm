def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()
    # 2
    for n in new_id:
        if n.islower() or n.isdigit() or n in ['-', '_', '.']:
            answer += n
    # 3
    while ".." in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if len(answer) == 0:
        answer = 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15]

    # 7
    if len(answer) <= 2:
        s = answer[-1]
        while len(answer) == 3:
            answer += s

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))