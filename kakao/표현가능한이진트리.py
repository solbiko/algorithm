import math

def search(n):
    length = len(n)
    mid = length // 2

    if length == 1 or '1' not in n or '0' not in n:
        return True


    if n[mid] == '0':
        return False

    return search(n[mid + 1:]) and search(n[:mid])


def solution(numbers):
    answer = []

    # 1. 이진수 변환
    bin_numbers = [bin(i)[2:] for i in numbers]

    for n in bin_numbers:

        # 2. 자릿수 변환

        # 노드갯수 len(n)
        # 트리높이 int(math.log(len(n), 2))
        # 포화이진트리 2ᴷ-1, 비어있으면 앞에 0추가
        digit = 2 ** (int(math.log(len(n), 2)) + 1) - 1
        n = "0" * (digit - len(n)) + n

        answer.append(1 if search(n) else 0)

    return answer

print(solution([58, 7, 42, 5, 63, 111, 95]))

