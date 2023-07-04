"""
1. answer의 값을 주식의 가격이 떨어지지 않았을 경우로 초기화한다.
2. rices를 순회하며 stack의 top의 인덱스보다 현재 price의 값이 작을 경우,
pop후, answer값을 수정하는 것을 반복한다.
"""
def solution(prices):
    n = len(prices)

    answer = [i for i in range(n-1,-1,-1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, n):
        while stack and prices[stack[-1]] > prices[i]: # 스택 맨 위
            j = stack.pop()
            answer[j]=i-j
        stack.append(i)
    return answer

print(solution(	[1, 2, 3, 2, 3]))

