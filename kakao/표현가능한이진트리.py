"""
이진트리에서 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브트리의 노드들보다 오른쪽에 있으며,
자신의 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정합니다.
numbers에 주어진 순서대로 하나의 이진트리로 해당 수를 표현할 수 있다면 1을, 표현할 수 없다면 0

1 ≤ numbers의 길이 ≤ 10,000
1 ≤ numbers의 원소 ≤ 1015

"""
import math

# 이진검색
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

        # 트리높이 int(math.log(len(n), 2))
        tree_height = int(math.log(len(n), 2))

        # 포화이진트리 노드개수 2ᴷ-1
        digit = 2**(tree_height+1)-1

        # 이진트리에 빈공간 있으면 앞에 0추가
        n = "0"*(digit-len(n)) + n

        answer.append(1 if search(n) else 0)

    return answer

print(solution([58, 7, 42, 5, 63, 111, 95]))

